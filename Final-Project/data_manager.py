import json

class DataManager:
    def __init__(self, path = 'Final-Project/data.json'):
        self.path = path

    
    def get(self):
        try:
            with open(self.path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.path, 'w') as f:
                json.dump({}, f)
            return {}
    
    def set(self, data):
        try:
            with open(self.path, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving data: {e}")
