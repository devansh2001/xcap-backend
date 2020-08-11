import json, yaml
from random import randint

class QuestionsFactory: 
    def __init__(self, apps_and_permissions):
        self.apps_and_permissions = apps_and_permissions

    def choose_application(self):
        if self.apps_and_permissions is None:
            return 'SAMPLE_APPLICATION'
        keys = list(self.apps_and_permissions.keys())
        index = randint(0, len(keys))
        print('Returning ---> ' + keys[index])
        return keys[index]

    def choose_permission(self, app):
        if self.apps_and_permissions is None:
            return 'SAMPLE_PERMISSION'
        values = list(self.apps_and_permissions.values())
        index = randint(0, len(values))
        print('Returning ---> ' + values[index])
        return values[index]

    def choose_benign_purpose(self, permission):
        return 'SAMPLE_BENIGN_PURPOSE'

    def choose_malicious_purpose(self, permission):
        return 'SAMPLE_MALICIOUS_PURPOSE'

    def produce_cleaned_question(self, text, variables):
        application = self.choose_application()
        permission = self.choose_permission(application)
        purpose = self.choose_benign_purpose(permission)
        if 'APPLICATION_NAME' in variables:
            text = text.replace('APPLICATION_NAME', application)
        if 'PERMISSION_REQUEST_CANONICALIZATION' in variables:
            text = text.replace('PERMISSION_REQUEST_CANONICALIZATION', permission)
        if 'PURPOSE' in variables:
            text = text.replace('PURPOSE', purpose)
        print('Returning ---> ' + text)
        return text

    def load_questions(self):
        data = None
        with open(r'./questions.yaml') as file:
            file = yaml.safe_load(file)
            data_str = json.dumps(file, indent=2)
        data_dict = json.loads(data_str)
        questions = data_dict['questions']

        # out = []
        for i in range(0, len(questions)):
            question = questions[i]
            text = question['text']

            if 'variables' in question:
                variables = question['variables']
                print(variables)
                text = self.produce_cleaned_question(text, variables)
                print(text)
                question['text'] = text
                questions[i] = question
        print(questions)
        data_dict['questions'] = questions

        for i in range(0, len(questions)):
            data_dict['questions'][i]['question_id'] = 'question_' + str(i + 1)

        print("********")
        print(data_dict)

        return json.dumps(data_dict)
        

    def generate_questions(self):
        # app = self.choose_application()
        # permission = self.choose_permission(app)
        # benign = self.choose_benign_purpose(permission)
        # malicious = self.choose_malicious_purpose(permission)
        # return []
        return self.load_questions()