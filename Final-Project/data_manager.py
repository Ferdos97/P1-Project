import json

class DataManager:
    def __init__(self, path = 'Final-Project/data.json'):
        self.path = path
        
    # def get(self):
    #     with open(self.path, 'r') as f:
    #         return json.load(f)
    
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

# import os
# import json

# class DataManager:
#     def __init__(self, path='Final-Project/data.json'):
#         self.path = path

#     def get(self):
#         try:
#             with open(self.path, 'r') as f:
#                 return json.load(f)
#         except FileNotFoundError:
#             os.makedirs(os.path.dirname(self.path), exist_ok=True)
#             with open(self.path, 'w') as f:
#                 json.dump({}, f)
#             return {}

#     def set(self, data):
#         try:
#             os.makedirs(os.path.dirname(self.path), exist_ok=True)
#             with open(self.path, 'w') as f:
#                 json.dump(data, f)
#         except Exception as e:
#             print(f"Error saving data: {e}")

