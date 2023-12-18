from flask import Flask, render_template, request, jsonify
import test_questions
import text_and_speech
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST', 'GET'])
def start():
    questions = [
        "What is the current year?",
        "what is the current season?",
        "What is the date today?",
        "What is the current day of the week?",
        "What is the current month?"
    ]

    return jsonify({"questions": questions})

@app.route('/ask_and_listen', methods=['POST', 'GET'])
def listen():
    data = request.get_json()
    question = data['question']
    subprocess.call(["espeak", question])
    spoken_text = text_and_speech.convert_speech_to_text()
    return jsonify({"spoken_text": spoken_text})


if __name__ == "__main__":
    app.run(debug=True)