import json

from src.context.variables import HealingKey, StatusBarKey

FILE_NAME = "config.json"
context = {
    "status_bar": {
        StatusBarKey.HP_PERCENT.value: 0,
        StatusBarKey.MP_PERCENT.value: 0,
    },
    "healing":
        {
            HealingKey.MP_HEAL_KEY.value: "",
            HealingKey.MP_MIN_PERCENT.value: 0,
            HealingKey.HP_HEAL_KEY.value: "",
            HealingKey.HP_MIN_PERCENT.value: 0
        },
}


def read_config():
    try:
        with open(FILE_NAME, 'r') as config_file:
            return json.load(config_file)
    except  (FileNotFoundError, json.JSONDecodeError):
        return context


class Context:
    file_name = FILE_NAME
    context = context

    def __init__(self):
        self.context = read_config()

    def save_config(self):
        with open(FILE_NAME, 'w') as config_file:
            json.dump(self.context, config_file, indent=4)

    def get_healing(self, key: HealingKey, default=None):
        return self.context['healing'].get(key.value, default)

    def set_healing(self, key: HealingKey, value):
        self.context['healing'][key.value] = value

    def get_status_bar(self, key: StatusBarKey, default=None):
        return self.context['status_bar'].get(key.value, default)

    def set_status_bar(self, key: StatusBarKey, value):
        self.context['status_bar'][key.value] = value
