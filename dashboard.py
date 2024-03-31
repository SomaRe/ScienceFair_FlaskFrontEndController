from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

# Load the dummy data
with open('static/dashboard_data.json', 'r') as f:
    data = json.load(f)

patients = list(data.keys())
score_data = json.dumps(data)

@app.route('/')
def index():
    return render_template('dashboard.html', patients=patients, score_data=score_data)

@app.route('/patient/<patient_name>', methods=['GET'])
def get_patient_details(patient_name):
    if patient_name in data:
        patient_data = data[patient_name]
        return jsonify(patient_data)
    else:
        return jsonify({'error': 'Patient not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5050)