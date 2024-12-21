import requests, json
from flask import jsonify

def emotion_detector(txt):
    text_to_analyze = txt
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers = headers, json = data)
    if response.status_code == 200:
        response_object = response.json()
        emotion_data = response_object['emotionPredictions'][0]['emotion']
        highest_val = 0
        most_significant_emotion = ''
        #Finding out the value of the most significant emotion
        for value in emotion_data.values():
            if highest_val < value:
                highest_val = value

        for key,value in emotion_data.items():
            if highest_val == value:
                most_significant_emotion = key

        emotion_data.update({'dominant emotion':most_significant_emotion})       
        return jsonify(emotion_data)
    else:
        return f"Error: {response.status_code}, {response.text}"

    


