import os
import openai

from openai_token import OPENAI_TOKEN

openai.api_key = OPENAI_TOKEN

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an incdent response specialist of the SANS framework helping people to analyse their incidents"},
    {"role": "user", "content": "What can you offer me?"}
  ]
)

print(completion.choices[0].message)