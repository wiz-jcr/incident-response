from django.shortcuts import render
from .models import Menu, Setting, Incident

# Create your views here.
stage_map  = {
    1: "Identification",
    2: "Containment",
    3: "Eradication",
    4: "Recovery",
    5: "Lessons Learned"
}

def index(request):
    menu = Menu.objects.all()
    setting = Setting.objects.all()
    incident = Incident.objects.all().order_by('-time_stamp')
    for entry in incident:
        entry.stage_name = stage_map[entry.stage]
        temp = []
        for i in range(1, entry.stage):
            temp.append(stage_map[i])
        entry.finished = temp.copy()
    render_dict = {
        'menulist': menu,
        'settinglist': setting,
        'dashboard-data': [],
        'incidentlist': incident
    }
    return render(request, 'index.html', render_dict)