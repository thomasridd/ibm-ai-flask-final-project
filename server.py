from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render 'index.html'

# Define a route for handling form submissions or API requests
@app.route('/emotionDetector', methods=['GET'])
def submit():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    return process_response(response)

def process_response(response):
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)