from flask import Flask, render_template, request, jsonify
import test_questions
import text_and_speech
import subprocess
import json
import time
import datetime

app = Flask(__name__)

data = {}

three_things = ()

def save_data_to_file():
    print(data)
    with open('results.json', 'r') as f:
        try:
            results = json.load(f)
        except:
            results = {}
    results[str(datetime.datetime.now())] = data
    with open('results.json', 'w') as f:
        json.dump(results, f)



def speak(text, default_model = "gTTS"):
    if default_model == "espeak":
        subprocess.call(["espeak", text])
    elif default_model == "gTTS":
        text_and_speech.convert_text_to_speech(text)

@app.route('/')
def index():
    data.clear()
    return render_template('index.html')

@app.route('/start', methods=['POST', 'GET'])
def start():

    global three_things
    three_things = ()
    instruction = "I will ask you some questions, and give you some problems to solve. Please answer them to the best of your ability."
    speak(instruction)
    time.sleep(1)

    questions = [
        "What is the current year?",
        "what is the current season?",
        "What is the date today?",
        "What is the current day of the week?",
        "What is the current month?",
        "What country are we in?",
        "What county are we in?",
        "What city are we in?",
    #     "What is the name or address of this building?",
    #     "What floor of the building are we on?",
    ]

    for q in questions:
        speak(q)
        spoken_text = text_and_speech.convert_speech_to_text()
        data[q] = spoken_text

    return jsonify({"data": data})

@app.route('/group2', methods=['POST', 'GET'])
def group2():
    global three_things
    instruction = 'I am going to name 3 objects. After I have said them I want you to repeat them back to me'
    speak(instruction)
    time.sleep(2)

    three_things = test_questions.get_three_things()
    speak(three_things[0] + '. ' + three_things[1] + '. And ' + three_things[2])
    time.sleep(1)
    speak("Please repeat now.")

    spoken_text = text_and_speech.convert_speech_to_text()
    data['three_things'] = {
        'spoken_text': spoken_text,
        'correct': " ".join(three_things)
    }
    time.sleep(1)
    speak("Repeat them few more times and try to remember, I will ask you to repeat them in few minutes.")
    time.sleep(10)


    return jsonify(data['three_things'])

@app.route('/group3', methods=['POST', 'GET'])
def group3():
    instruction = "Now I am going to give you a word, and I want you to say it backwards."
    speak(instruction)
    time.sleep(1)
    word = test_questions.get_reverse_word()
    speak("The word is: " + word)

    spoken_text = text_and_speech.convert_speech_to_text(model = "google")
    print(spoken_text)
    data['reverse_word'] = {
        'spoken_text': spoken_text,
        'correct': word[::-1]
    }

    return jsonify(data['reverse_word'])

@app.route('/group4', methods=['POST', 'GET'])
def group4():
    instructions = "Can you repeat the three things I asked you to remember earlier?"
    speak(instructions)
    time.sleep(1)

    spoken_text = text_and_speech.convert_speech_to_text()
    data['three_things_repeat'] = {
        'spoken_text': spoken_text,
        'correct': " ".join(three_things)
    }
    
    save_data_to_file()

    return jsonify(data['three_things_repeat'])



if __name__ == "__main__":
    app.run(debug=True)