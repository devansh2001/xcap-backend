from flask import Flask, request
from flask_cors import CORS
import json
import pyrebase
import QuestionsFactory
from config import firebaseConfig

app = Flask(__name__)
CORS(app, support_credentials=True)

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

@app.route('/')
def test():
    print('hello')
    return 'Hello, World!'

@app.route('/get-questions', methods=['POST'])
def get_questions():
    print("hey")
    
    apps_and_permissions = None
    if request.data:
        apps_and_permissions = json.loads(request.data)
    # print(apps_and_permissions)
    factory = QuestionsFactory.QuestionsFactory(apps_and_permissions)
    questions = factory.generate_questions()
    return questions


@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    print('Hit Submit Survey Endpoint')
    data = None
    print(request.data)
    if request.data:
        data = json.loads(request.data)
    
    print('Received data:')
    print(data)

    database.child('test')
    database.set(data)

    return {}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)