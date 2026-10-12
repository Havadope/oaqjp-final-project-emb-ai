import requests
import json

def emotion_detector(text_to_analyze):
    #Define the URL for the emotion detector API
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": 
    "emotion_aggregated-workflow_lang_en_stock"}

    #How to input the info in json file
    input_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=input_json)

    return response.text

