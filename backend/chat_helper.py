import openai
import json
from pathlib import Path

system_prompt = Path('./system_prompt.txt').read_text()
system_prompt = system_prompt.replace('\n', '')

class ChatHelper:
    def __init__(self, api_key, index, user_id):
        self.index = index
        openai.api_key = api_key
        self.user_id = user_id
        self.chat_history = []
        self.filename = f"{self.user_id}_chat_history.json"

    def generate_response(self, user_input):
        prompt = [{"role": "system", "content": system_prompt}]
        if self.chat_history:
            for message in self.chat_history[-5:]:
                prompt.append(message)
        prompt.append({"role": "user", "content": "{}".format(user_input)})
        
        # query_engine = self.index.as_query_engine()
        
        # response = query_engine.query(user_input)
        completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=prompt,
                    name = "IncidentArmor",
                    max_tokens = 50,
                    temperature = 0.2
                    )
        response = completion.choices[0].message
        message = {"role": "assistant", "content": response["content"]}
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message
    
    def load_chat_history(self):
        try:
            with open(self.filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self):
        with open(self.filename, 'w') as f:
            json.dump(self.chat_history, f)