from flask import Flask, render_template, request, jsonify
import test_questions
import text_and_speech
import subprocess
import json
import time
import random
import datetime

app = Flask(__name__)

data = {}
three_things = ()
image_data1 = ()
image_data2 = ()
words = ()
chosen_word = ""
clock = {}

def save_data_to_file():
    print(data)
    try:
        with open('results.json', 'r') as f:
            results = json.load(f)
    except:
        # create file
        results = {}
    results[str(datetime.datetime.now())] = data
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)



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

    global three_things, image_data1, image_data2, data, words, chosen_word, clock
    data = {}
    three_things = ()
    image_data1 = ()
    image_data2 = ()
    words = ()
    chosen_word = ""
    clock = {}
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
        # "What county are we in?",
        # "What city are we in?",
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

    spoken_text = text_and_speech.convert_speech_to_text()
    data['three_things'] = {
        'spoken_text': spoken_text,
        'correct': " ".join(three_things)
    }
    time.sleep(1)
    speak("Repeat them few more times and try to remember, I will ask you to repeat them in few minutes.")
    time.sleep(10)


    return jsonify(data)

@app.route('/group3', methods=['POST', 'GET'])
def group3():
    instruction = "Now I am going to give you a word, and I want you to say it backwards."
    speak(instruction)
    time.sleep(1)
    word = test_questions.get_reverse_word()
    speak("The word is: " + word)

    spoken_text = text_and_speech.convert_speech_to_text()
    print(spoken_text)
    data['reverse_word'] = {
        'spoken_text': spoken_text.replace(" ", ""),
        'correct': word[::-1]
    }

    return jsonify(data)

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

    return jsonify(data)

@app.route('/group5_1', methods=['POST', 'GET'])
def group5_1():
    global image_data1
    image_data1= test_questions.get_image_link()

    return jsonify(image_data1)

@app.route('/group5_2', methods=['POST', 'GET'])
def group5_2():
    instructions = "Name the object in the picture."
    speak(instructions)
    time.sleep(1)

    spoken_text = text_and_speech.convert_speech_to_text()
    data['image1'] = {
        'spoken_text': spoken_text,
        'correct': image_data1[0]
    }

    return jsonify(data)

# lets repeat the same thing for the second image, group5_1_repeat and group5_2_repeat
@app.route('/group5_1_repeat', methods=['POST', 'GET'])
def group5_1_repeat():
    global image_data2
    while True:
        image_data2 = test_questions.get_image_link()
        if image_data2[0] != image_data1[0]:
            break

    return jsonify(image_data2)

@app.route('/group5_2_repeat', methods=['POST', 'GET'])
def group5_2_repeat():
    instructions = "Now name this object"
    speak(instructions)
    time.sleep(1)

    spoken_text = text_and_speech.convert_speech_to_text()
    data['image2'] = {
        'spoken_text': spoken_text,
        'correct': image_data2[0]
    }

    return jsonify(data)

@app.route('/group6', methods=['POST', 'GET'])
def group6():
    instructions = "I would like you to repeat the following phrase after me: No ifs, ands, or buts."
    speak(instructions)

    spoken_text = text_and_speech.convert_speech_to_text()
    data['phrase'] = {
        'spoken_text': spoken_text,
        'correct': "No ifs, ands, or buts"
    }

    return jsonify(data)


@app.route('/group7_1', methods=['POST', 'GET'])
def group7_1():
    global words, chosen_word
    instructions = "Read the instructions on the screen and do what it says."
    speak(instructions)

    words = test_questions.get_words_to_click()
    chosen_word = random.choice(words)
    return jsonify(words, chosen_word)

@app.route('/group7_2', methods=['POST', 'GET'])
def group7_2():
    if request.method == 'POST':
        r = request.get_json()
        result = r['target']

        data['words'] = {
            'chosen_word': result,
            'correct': chosen_word
        }

    return jsonify(data)

@app.route('/group8_1', methods=['POST', 'GET'])
def group8_1():
    global clock
    instructions = "I am going to give you a time, please use the sliders on screen to set the time to the given time."
    speak(instructions)
    time.sleep(0.5)

    clock = test_questions.get_random_time()
    speak(f"The time is {clock['hour']} {clock['minute']}")

    return jsonify(clock)

@app.route('/group8_2', methods=['POST', 'GET'])
def group8_2():
    if request.method == 'POST':
        r = request.get_json()
        r['hour'] = 12 if int(r['hour'])//30 == 0 else int(r['hour'])//30
        r['minute'] = int(r['minute'])//6

        data['clock'] = {
            'time': r,
            'correct': clock
        }

    save_data_to_file()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)