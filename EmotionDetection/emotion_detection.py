import requests

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, headers=HEADERS, json=body)

    if response.status_code == 200:
        return format_response(response.json())
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return {
            'error': 'Failed to analyse emotion',
            'status_code': response.status_code
        }

def format_response(response):
    emotion = response['emotionPredictions'][0]['emotion']
    dominant = get_dominant(emotion)

    return {
        'anger': emotion['anger'],
        'disgust': emotion['disgust'],
        'fear': emotion['fear'],
        'joy': emotion['joy'],
        'sadness': emotion['sadness'],
        'dominant_emotion': dominant
    }

def get_dominant(emotion_values):
    dominant = 'anger'
    for emotion in ['disgust', 'fear', 'joy', 'sadness']:
        if emotion_values[emotion] > emotion_values[dominant]:
            dominant = emotion
    return dominant