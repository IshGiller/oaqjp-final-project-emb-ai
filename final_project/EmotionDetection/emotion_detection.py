import json
import requests


def emotion_detector(text_to_analyze):
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    my_obj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    header = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(
        url,
        json=my_obj,
        headers=header
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    result = json.loads(response.text)
    scores = result["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(scores, key=scores.get)

    return {
        "anger": scores["anger"],
        "disgust": scores["disgust"],
        "fear": scores["fear"],
        "joy": scores["joy"],
        "sadness": scores["sadness"],
        "dominant_emotion": dominant_emotion
    }