import json

from shared.typings import GrayImage
from src.context.variables import HealingKey, StatusBarKey, BattleListKey

FILE_NAME = "config.json"
config = {
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
    except (FileNotFoundError, json.JSONDecodeError):
        return config


class Context:
    file_name = FILE_NAME
    config = config
    _screenshot: GrayImage = None
    _battle_list = {
        BattleListKey.CREATURES: []
    }

    def __init__(self):
        self.config = read_config()

    def get_screenshot(self):
        return self._screenshot

    def set_screenshot(self, screenshot: GrayImage):
        self._screenshot = screenshot

    def save_config(self):
        with open(FILE_NAME, 'w') as config_file:
            json.dump(self.config, config_file, indent=4)

    def get_healing(self, key: HealingKey, default=None):
        return self.config['healing'].get(key.value, default)

    def set_healing(self, key: HealingKey, value):
        self.config['healing'][key.value] = value

    def get_status_bar(self, key: StatusBarKey, default=None):
        return self.config['status_bar'].get(key.value, default)

    def set_status_bar(self, key: StatusBarKey, value):
        self.config['status_bar'][key.value] = value

    def get_battle_list(self, key: BattleListKey, default=None):
        return self._battle_list.get(key.value, default)

    def set_battle_list(self, key: BattleListKey, value):
        self._battle_list[key.value] = value
