import os
import sys
import azure.cognitiveservices.speech as speechsdk
import requests
import json
import openai

from temboo.Library.Google.Gmail import SendEmail
from temboo.core.session import TembooSession

#SETUP

#GPT 3 API key
openai.api_key = "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"
#initialize prompt
prompt = "Say this is a test."


#Azure API function speech-to-text
def recognize_from_microphone(prompt):
    speech_config = speechsdk.SpeechConfig(subscription="23ed5e365f4842b8911a3d03355826ae", region="eastus")
    speech_config.speech_recognition_language="en-US"

    #To recognize speech from an audio file, use `filename` instead of `use_default_microphone`:
    #audio_config = speechsdk.audio.AudioConfig(filename="YourAudioFile.wav")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Recording...")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        prompt = speech_recognition_result.text
        print("Recognized: {}".format(speech_recognition_result.text))
        return prompt
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))


#Store s2t response
speech = recognize_from_microphone(prompt)

#Request GPT3 with text from transcription
try:
  response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=speech,
  temperature=1,
  max_tokens=224,
  top_p=1,
  frequency_penalty=0.31,
  presence_penalty=0.15
  )
  answer = response
except requests.RequestException:
  print("ERROR: Not able to contact OpenAI API")

#parsing JSON from GPT3
gossip = answer['choices'][0]['text']

#setup variables 
payload = {'text': gossip,}
webhook_url = "https://hooks.slack.com/services/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"

#slack post function
def post_gossip(payload, webhook_url):
   return requests.post(webhook_url, json.dumps(payload))

#call slack post function
post_gossip(payload, webhook_url)
