from flask import Flask, request
import QuestionsFactory
app = Flask(__name__)

@app.route('/')
def test():
    return 'Hello, World!'

@app.route('/get-questions')
def get_questions():
    apps_and_permissions = request.data
    factory = QuestionsFactory.QuestionsFactory(None)
    questions = factory.generate_questions()
    return questions


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)