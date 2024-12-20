import json

response_object = {
            'emotionPredictions': [
                {
                    'emotion': {
                        'anger': 0.0043339236,
                        'disgust': 0.00037549555,
                        'fear': 0.0034732423,
                        'joy': 0.9947189,
                        'sadness': 0.012704818
                    },
                    'target': '',
                    'emotionMentions': [
                        {
                            'span': {
                                'begin': 0,
                                'end': 30,
                                'text': 'I am so happy I am doing this.'
                            },
                            'emotion': {
                                'anger': 0.0043339236,
                                'disgust': 0.00037549555,
                                'fear': 0.0034732423,
                                'joy': 0.9947189,
                                'sadness': 0.012704818
                            }
                        }
                    ]
                }
            ],
            'producerId': {
                'name': 'Ensemble Aggregated Emotion Workflow',
                'version': '0.0.1'
            }
}

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

print("emotion: {")
for key, value in emotion_data.items():
    print(f"\t{key}: {value}")
print("\tdominant_emotion:", f"{most_significant_emotion}")
print("}")

