import os
import sys
import requests
import json
import openai
#https://jman4190.medium.com/how-to-build-a-gpt-3-chatbot-with-python-7b83e55805e6
#https://python.plainenglish.io/create-ai-content-generator-with-python-flask-and-openai-gpt-3-407a19f096b
#https://slacker.ro/2020/08/28/the-ultimate-guide-to-openais-gpt-3-language-model/

#AP
openai.api_key = "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"


#input prompt
prompt = "Say this is a test."

#request

try:
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  temperature=1,
  max_tokens=224,
  top_p=1,
  frequency_penalty=0.31,
  presence_penalty=0.15
  )
  answer = response
except requests.RequestException:
  print("ERROR: Not able to contact OpenAI API")

#parsing JSON 
gossip = answer['choices'][0]['text']

print(gossip)
#print(answer)