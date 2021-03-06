from flask import Flask, request
from flask_cors import CORS
import json
import pyrebase
import QuestionsFactory
import datetime
import os
# from config import firebaseConfig

app = Flask(__name__)
CORS(app, support_credentials=True)
# print(firebaseConfig)
firebaseConfig = {
    "apiKey": os.environ['apiKey'],
    "authDomain": os.environ['authDomain'],
    "databaseURL": os.environ['databaseURL'],
    "projectId": os.environ['projectId'],
    "storageBucket": os.environ['storageBucket'],
    "serviceAccount": {
        "type": os.environ['type'],
        "project_id": os.environ['project_id'],
        "private_key_id": os.environ['private_key_id'],
        "private_key": os.environ['private_key'].replace('\\n', '\n'),
        "client_email": os.environ['client_email'],
        "client_id": os.environ['client_id'],
        "auth_uri": os.environ['auth_uri'],
        "token_uri": os.environ['token_uri'],
        "auth_provider_x509_cert_url": os.environ['auth_provider_x509_cert_url'],
        "client_x509_cert_url": os.environ['client_x509_cert_url']
    },
    "messagingSenderId": os.environ['messagingSenderId'],
    "appId": os.environ['appId'],
    "measurementId": os.environ['measurementId']
}
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()

@app.route('/')
def test():
    print('hello')
    return 'Hello, World!'

@app.route('/get-questions', methods=['POST'])
def get_questions():
    # print("hey")
    
    apps_and_permissions = None
    if request.data:
        apps_and_permissions = json.loads(request.data)
    # print(apps_and_permissions)
    # print(type(apps_and_permissions))
    factory = QuestionsFactory.QuestionsFactory(apps_and_permissions)
    questions = factory.generate_questions()
    return questions


@app.route('/submit-survey', methods=['POST'])
def submit_survey():
    # print('Hit Submit Survey Endpoint')
    data = None
    # print(request.data)
    if request.data:
        data = json.loads(request.data)
    
    # print('Received data:')
    # print(data)

    save_object = {}
    save_object['user_response'] = data['data']
    save_object['app'] = data['chosen_data']['app']
    save_object['permission'] = data['chosen_data']['permission']
    save_object['timestamp'] = str(datetime.datetime.now())

    # print(data['participant_id'])
    # print(save_object)
    database.child('data').child(data['participant_id']).push(save_object)

    return {}

some_id = 'unique_id_123'
@app.route('/try-pyrebase')
def try_pyrebase():
    some_data = {
        'name': 'ABC',
        'age': 15
    }
    database.child(some_id).push(some_data)
    return {}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)