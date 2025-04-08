import requests

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, headers=HEADERS, json=body)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            'error': 'Failed to analyse emotion',
            'status_code': response.status_code
        }
