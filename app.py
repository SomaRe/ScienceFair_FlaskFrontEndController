from flask import Flask, render_template, request, jsonify
import test_questions
import text_and_speech
import subprocess
import time

app = Flask(__name__)

data = {}

def speak(text, default_model = "gTTS"):
    if default_model == "espeak":
        subprocess.call(["espeak", text])
    elif default_model == "gTTS":
        text_and_speech.convert_text_to_speech(text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST', 'GET'])
def start():

    instructions = "I will ask you some questions. Please answer them to the best of your ability."
    speak(instructions)
    time.sleep(2)

    questions = [
        "What is the current year?",
        "what is the current season?",
        "What is the date today?",
        "What is the current day of the week?",
        "What is the current month?"
    ]

    for q in questions:
        speak(q)
        spoken_text = text_and_speech.convert_speech_to_text()
        data[q] = spoken_text
        print(spoken_text)

    return jsonify({"questions": questions})


if __name__ == "__main__":
    app.run(debug=True)