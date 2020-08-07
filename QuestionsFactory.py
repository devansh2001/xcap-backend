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
        with open(r'./questions.yaml') as file:
            file = yaml.safe_load(file)
            return json.dumps(file, indent=2)

    def generate_questions(self):
        app = self.choose_application()
        permission = self.choose_permission(app)
        benign = self.choose_benign_purpose(permission)
        malicious = self.choose_malicious_purpose(permission)
        return []