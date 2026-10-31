"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():

    """Analyze the text supplied to the emotion detector."""

    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )



@app.route("/")
def render_index_page():

    ''' This function initiates the rendering of the main application
    page over the Flask channel
    '''

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
