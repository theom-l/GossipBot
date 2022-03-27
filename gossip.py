import os
import sys
import requests
import json
import openai
import azure.cognitiveservices.speech as speechsdk

from temboo.Library.Google.Gmail import SendEmail
from temboo.core.session import TembooSession


#https://jman4190.medium.com/how-to-build-a-gpt-3-chatbot-with-python-7b83e55805e6
#https://python.plainenglish.io/create-ai-content-generator-with-python-flask-and-openai-gpt-3-407a19f096b
#https://slacker.ro/2020/08/28/the-ultimate-guide-to-openais-gpt-3-language-model/

#API
openai.api_key = "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"


#input prompt
prompt = "Say this is a test."

#request

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription="23ed5e365f4842b8911a3d03355826ae", region="eastus")
    speech_config.speech_recognition_language="en-US"

    #To recognize speech from an audio file, use `filename` instead of `use_default_microphone`:
    #audio_config = speechsdk.audio.AudioConfig(filename="YourAudioFile.wav")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Recording...")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        prompt = format(speech_recognition_result.text)
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

recognize_from_microphone()

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

# def sendEmail():
#   # Create a session with your Temboo account details
#   session = TembooSession("theom-l", "myFirstApp", "Sa4XQ0WCr0z48pV8cTv8PPbJwL8gI9n5")

#   # Instantiate the Choreo
#   sendEmailChoreo = SendEmail(session)

#   # Get an InputSet object for the Choreo
#   sendEmailInputs = sendEmailChoreo.new_input_set()

#   # Set the Choreo inputs
#   sendEmailInputs.set_Username("gb123988124123@gmail.com")
#   sendEmailInputs.set_Subject("1")
#   sendEmailInputs.set_ToAddress("emandinl@andrew.cmu.edu")
#   sendEmailInputs.set_Password("tpylvnfhlmuscdzo")
#   sendEmailInputs.set_MessageBody("1")

#   # Execute the Choreo
#   sendEmailResults = sendEmailChoreo.execute_with_results(sendEmailInputs)

#   # Print the Choreo outputs
#   print("Success: " + sendEmailResults.get_Success())

# sendEmail()