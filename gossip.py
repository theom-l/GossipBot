import os
import sys
import requests
import json
import openai

from temboo.Library.Google.Gmail import SendEmail
from temboo.core.session import TembooSession


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

#print(answer)

def sendEmail(gossip):
  # Create a session with your Temboo account details
  session = TembooSession("theom-l", "myFirstApp", "LDlj0THtgAYNMjHJxhgpCWsI49Vfwuli")

  # Instantiate the Choreo
  sendEmailChoreo = SendEmail(session)

  # Get an InputSet object for the Choreo
  sendEmailInputs = sendEmailChoreo.new_input_set()

  # Set the Choreo inputs
  sendEmailInputs.set_Username("gb123988124123@gmail.com")
  sendEmailInputs.set_Subject(" ")
  sendEmailInputs.set_ToAddress("emandinl@andrew.cmu.edu")
  sendEmailInputs.set_Password("tpylvnfhlmuscdzo")
  sendEmailInputs.set_MessageBody(gossip)

  # Execute the Choreo
  sendEmailResults = sendEmailChoreo.execute_with_results(sendEmailInputs)

  # Print the Choreo outputs
  print("Success: " + sendEmailResults.get_Success())