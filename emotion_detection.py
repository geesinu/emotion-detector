import requests

def emotion_detector(text_to_analyse):
    # URL and Headers as specified in your JSON
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Input JSON data
    data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Make the request
    response = requests.post(url, json=data, headers=headers)

    emotion = response.json()['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion, key=emotion.get)
    emotion['dominant_emotion'] = dominant_emotion
    return emotion
    

# # Example usage
# text_to_analyse = "I love this new technology."
# result = emotion_detector(text_to_analyse)
# print(result)
