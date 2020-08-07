import json, yaml
class QuestionsFactory: 
    def __init__(self, apps_and_permissions):
        self.apps_and_permissions = apps_and_permissions

    def choose_application(self):
        return ''

    def choose_permission(self, app):
        return ''

    def choose_benign_purpose(self, permission):
        return ''

    def choose_malicious_purpose(self, permission):
        return ''

    def produce_cleaned_question(self, text, variables):
        return ''

    def load_questions(self):
        data = None
        with open(r'./questions.yaml') as file:
            file = yaml.safe_load(file)
            data_str = json.dumps(file, indent=2)
        data_dict = json.loads(data_str)
        questions = data_dict['questions']

        out = []
        for question in questions:
            text = question['text']
            if 'variables' in question:
                variables = question['variables']
                print(variables)
                text = self.produce_cleaned_question(text, variables)



        return json.dumps(data_dict)
        

    def generate_questions(self):
        # app = self.choose_application()
        # permission = self.choose_permission(app)
        # benign = self.choose_benign_purpose(permission)
        # malicious = self.choose_malicious_purpose(permission)
        # return []
        return self.load_questions()