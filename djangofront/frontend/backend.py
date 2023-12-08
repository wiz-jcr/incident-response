import os
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
load_dotenv()
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex
from .chat_helper import ChatHelper
from .openai_token import OPENAI_TOKEN
from .stage_script import PLAYBOOK
from .models import *
from .serializers import *

os.environ["OPENAI_API_KEY"] = OPENAI_TOKEN
# Create your views here.
stage_map  = {
    1: "Identification",
    2: "Containment",
    3: "Eradication",
    4: "Recovery",
    5: "Lessons Learned"
}

loader = SimpleDirectoryReader('./static/data', required_exts='*.txt')
documents = loader.load_data()
# load index
index = GPTVectorStoreIndex.from_documents(documents)

class IncidentListCreateView(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    
@api_view(['GET'])
def get_incident(request):
    incident = Incident.objects.all().order_by('-time_stamp')
    resp = [IncidentSerializer(entry).data for entry in incident ]
    return Response(resp)

@api_view(['GET'])
def get_incident_detail(request, id):
    try:
        incident = Incident.objects.get(id=id)
    except Incident.DoesNotExist:
        return Response({'error': 'Incident not found'}, status=404)

    serializer = IncidentSerializer(incident)
    resp = serializer.data
    resp["stage_name"] = stage_map[resp["stage"]]
    resp["finished"] = []
    for i in range(1, resp["stage"]):
        resp["finished"].append(stage_map[i])
        
    resp["playbook"] = "Lorem Ipsum"
    
    if resp["type"] in PLAYBOOK:
        resp["playbook"] = PLAYBOOK[resp["type"]][str(resp["stage"])]
    
    action = []
    if resp["stage"] == 2:
        action.append("chat")
    elif resp["stage"] == 4:
        action.append("back")
    
    if resp["stage"] != 5:
        action.append("next")
    
    resp["action"] = action
    
    return Response(resp)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])  
def create_incident(request):
    id = request.data["id"]
    stage = 2
    type = request.data["type"]
    try:
        incident = Incident.objects.get(id=id)
        incident.type = type
        incident.stage = stage
        incident.save(update_fields=["type","stage"])
    except Incident.DoesNotExist:
        incident = Incident(id=id, stage=stage, type=type )
        incident.save()
    
    resp = {"msg": "Finished creating incident {}".format(id)}
    
    return Response(resp)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])  
def update_incident(request):
    id = request.data["id"]
    try:
        incident = Incident.objects.get(id=id)
    except Incident.DoesNotExist:
        return Response({'error': 'Incident not found'}, status=404)
    incident.stage = int(request.data["stage"])
    incident.save(update_fields=["stage"])
    
    resp = {"msg": "Finished updating incident {} to stage {}".format(id, incident.stage)}
    
    return Response(resp)

@api_view(['GET'])
def get_new_incident(request):
    id = Incident.objects.latest('id').id
    
    resp = { "id": id + 1 }
    
    return Response(resp)

@api_view(['GET'])
def retrieve_chat(request, id):
    
    chat_hist = ChatLog.objects.filter(uid=id).order_by('time_stamp')
    
    resp = {"msg": [ChatLogSerializer(entry).data for entry in chat_hist ]}
    return Response(resp)
    

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])  
def chat_input(request):
    chat_id = request.data["uid"]
    bot = ChatHelper( index, chat_id)

    # Load chat history
    bot.load_chat_history()

    # Generate response
    bot_response = bot.generate_response(request.data["msg"])
    bot_response_content = bot_response['content']
    resp = {'msg': bot_response_content,
            'link': ""}
    for incident in PLAYBOOK.keys():
        if incident in bot_response_content.lower():
            resp['link'] += '<br><a href="#" class="create-incident" incident="{}" type="{}">Create this incident</a>'.format(chat_id, incident)
    
    return Response(resp)