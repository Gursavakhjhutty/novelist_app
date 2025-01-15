import json

def save_project(project, filename):
    with open(filename, 'w') as f:
        json.dump(project._dict_, f)
def load_project(project, filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return Project(data["title"], data["genre"])