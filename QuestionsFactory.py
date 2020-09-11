import json, yaml
import ast
from random import randint

class QuestionsFactory: 
    def __init__(self, apps_and_permissions):
        self.apps_and_permissions = apps_and_permissions
        if self.apps_and_permissions is not None:
            self.apps_and_permissions.pop('PARTICIPANT_ID')
            self.chosen_application = self.choose_application()
            self.chosen_permission = self.choose_permission(self.chosen_application)
        else:
            self.chosen_application = 'SAMPLE_APPLICATION'
            self.chosen_permission = 'SAMPLE_PERMISSION'
            

    def choose_application(self):
        if self.apps_and_permissions is None:
            return 'SAMPLE_APPLICATION'
        keys = list(self.apps_and_permissions.keys())
        index = randint(0, len(keys) - 1)
        print('Returning ---> ' + keys[index])
        return keys[index]

    def choose_permission(self, app):
        if self.apps_and_permissions is None:
            return 'SAMPLE_PERMISSION'
        values = self.apps_and_permissions[app]
        print(values)
        values = yaml.safe_load(values)
        print(type(values))
        print('----------Converted----------')
        print(values)
        if len(values) == 0:
            return 'SAMPLE_PERMISSION'
        index = randint(0, len(values) - 1)
        print(len(values))
        print(index)
        print('Returning ---> ' + values[index])
        return values[index]

    def choose_canonicalization(self, permission):
        if self.apps_and_permissions is None or permission == 'SAMPLE_PERMISSION' or permission is None:
            return 'SAMPLE_PERMISSION_REQUEST_CANONICALIZATION'
        
        data = None
        with open(r'./permission_info.yaml') as file:
            file = yaml.safe_load(file)
            data_str = json.dumps(file, indent=2)
        data_dict = json.loads(data_str)
        return data_dict[permission]['CANONICALIZATION']

    def choose_benign_purpose(self, permission):
        if self.apps_and_permissions is None or permission == 'SAMPLE_PERMISSION' or permission is None:
            return 'SAMPLE_PERMISSION_REQUEST_CANONICALIZATION'
        
        data = None
        with open(r'./permission_info.yaml') as file:
            file = yaml.safe_load(file)
            data_str = json.dumps(file, indent=2)
        data_dict = json.loads(data_str)
        return data_dict[permission]['BENIGN']

    def choose_malicious_purpose(self, permission):
        if self.apps_and_permissions is None or permission == 'SAMPLE_PERMISSION' or permission is None:
            return 'SAMPLE_PERMISSION_REQUEST_CANONICALIZATION'
        
        data = None
        with open(r'./permission_info.yaml') as file:
            file = yaml.safe_load(file)
            data_str = json.dumps(file, indent=2)
        data_dict = json.loads(data_str)
        return data_dict[permission]['MALICIOUS']

    def produce_cleaned_question(self, text, variables):
        # application = self.choose_application()
        # permission = self.choose_permission(self.chosen_application)
        canonicalization = self.choose_canonicalization(self.chosen_permission)
        purpose = self.choose_benign_purpose(self.chosen_permission)
        if 'APPLICATION_NAME' in variables:
            text = text.replace('APPLICATION_NAME', self.chosen_application)
        if 'PERMISSION_REQUEST_CANONICALIZATION' in variables:
            text = text.replace('PERMISSION_REQUEST_CANONICALIZATION', canonicalization)
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

        data_dict['chosen_data'] = {
            'app': self.chosen_application,
            'permission': self.chosen_permission
        }
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