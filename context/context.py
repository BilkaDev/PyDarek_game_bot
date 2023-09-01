import json

FILE_NAME = "config.json"




class Context: 
    file_name = FILE_NAME
    def __init__(self):
        self.context = self.read_config()

    def save_config(self):
        with open(FILE_NAME, 'w') as config_file:
            json.dump(self.context, config_file, indent=4)

    def read_config(self):
        try:
            with open(FILE_NAME, 'r') as config_file:
                return json.load(config_file)
        except  (FileNotFoundError, json.JSONDecodeError):
            return {}

    def set(self,key: str, item):
        self.context[key] = item

    def get(self,key: str, default=None):
        return self.context.get(key, default)
