"""
This module provides routes for the application.

Functions:
- home: Renders the index page
- submit: Renders a response to the submitted form.
- process_response: Formats a standard emotion_detector response as text
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    """
    Renders the index page.

    Returns:
    - render_template: a rendered index page.
    """
    return render_template('index.html')  # Render 'index.html'

# Define a route for handling form submissions or API requests
@app.route('/emotionDetector', methods=['GET'])
def submit():
    """
    Renders a response to the submitted form.

    Returns:
    - response: A text response to be displayed on the index page
    """

    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!.'
    return process_response(response)

def process_response(response):
    """
    Formats a standard emotion_detector response as text

    Parameters:
    - response (dict): The standard emotion_detector dictionary

    Returns:
    - processed: A text version of the dictionary.
    """
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
