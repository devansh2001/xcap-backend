from flask import Flask, request
from flask_cors import CORS
import QuestionsFactory

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/')
def test():
    print('hello')
    return 'Hello, World!'

@app.route('/get-questions', methods=['POST'])
def get_questions():
    print("hey")
    apps_and_permissions = request.data
    factory = QuestionsFactory.QuestionsFactory(None)
    questions = factory.generate_questions()
    return questions


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)