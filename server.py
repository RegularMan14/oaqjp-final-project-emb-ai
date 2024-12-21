from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    print("For the given statement, the system response is ", end="")
    for label, item in response.items():
        if(label != "dominant emotion"):
            print(f"'{label}' : {item}")
        else:
            print(f". The dominant emotion is {item}")
            