from openai import OpenAI
from .openai_token import OPENAI_TOKEN
client = OpenAI(api_key=OPENAI_TOKEN)
from .stage_script import system_prompt
from .models import ChatLog

class ChatHelper:
    def __init__(self,index, uid):
        self.index = index
        self.uid = uid
        self.chat_history = []

    def generate_response(self, user_input):
        prompt = [{"role": "system", "content": "{}".format(system_prompt)}]
        if self.chat_history:
            for message in self.chat_history[-5:]:
                prompt.append(message)
        prompt.append({"role": "user", "content": "{}".format(user_input)})
        # write to db
        user_msg = ChatLog( uid = self.uid, role="user", content=user_input)
        user_msg.save()
        
        # query_engine = self.index.as_query_engine()
        
        # response = query_engine.query(user_input)
        completion = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=prompt,
        # name = "IncidentArmor",
        temperature = 0.2)
        content = completion.choices[0].message.content
        message = {"role": "assistant", "content": content}
        
        bot_msg = ChatLog( uid = self.uid, role="assistant", content=content)
        bot_msg.save()
        
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message
    
    def load_chat_history(self):
        try:
            chat_hist = ChatLog.objects.filter(uid=self.uid).order_by('-time_stamp')
            
            for entry in chat_hist:
                self.chat_history.append({"role": entry.role, "content": entry.content})
                if len(self.chat_history) > 5:
                    break
            
            self.chat_history.reverse()
        except ChatLog.DoesNotExist:
            pass