"""This module provides the function to find out the Emotion score"""
from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """Returns a Dictionary containing all the emotions"""
    text_to_analyze = request.args.get('textToAnalyze')
    dic = emotion_detector(text_to_analyze)
    dominant_emotion = None
    print("For the given statement, the system response is ", end="")
    result = {}
    for label, item in dic.items():
        if label != "dominant emotion":
            print(f"'{label}' : {item}", end=" ")
            result[label] = item
        else:
            result[label] = item
            dominant_emotion = item
    print(type(dominant_emotion))
    if dominant_emotion is None:
        print("Invalid Text! Please try again!")
    else:
        print(f". The dominant emotion is {dominant_emotion}")
    return result
