"""
This module provides a Flask application for detecting emotions from text.
It uses the emotion_detector function from the emotion_detection module.
"""

from flask import Flask, request, jsonify
try:
    from emotion_detection import emotion_detector
except ImportError:
    # Handle the import error gracefully or log it if necessary
    emotion_detector = None

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detects emotions from the provided text input. Returns a JSON response
    with the analysis or an error message.
    """
    if emotion_detector is None:
        return jsonify({'error': 'Emotion detection functionality is not available.'}), 500

    data = request.json
    text_to_analyse = data.get('text', '').strip()

    if not text_to_analyse:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    try:
        emotion_analysis = emotion_detector(text_to_analyse)
        response = f"For the given statement, the system response is {emotion_analysis}"
        return jsonify({'response': response})
    except ValueError as e:  # Replace ValueError with a more specific exception if applicable
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
