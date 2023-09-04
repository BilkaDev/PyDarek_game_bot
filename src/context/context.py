import json

from shared.typings import GrayImage
from src.context.variables import HealingKeys, StatusBarKeys, BattleListKeys, CavebotConfigKeys

FILE_NAME = "config.json"
config = {
    "healing":
        {
            HealingKeys.MP_HEAL_KEY.value: "",
            HealingKeys.MP_MIN_PERCENT.value: 0,
            HealingKeys.HP_HEAL_KEY.value: "",
            HealingKeys.HP_MIN_PERCENT.value: 0
        },
    "cavebot":
        {
            CavebotConfigKeys.AUTO_ATTACK_ENABLED: False,
            CavebotConfigKeys.MANA_TRAIN_ENABLED: False,
            CavebotConfigKeys.MANA_TRAIN_KEY: "",
            CavebotConfigKeys.MANA_TRAIN_MAX_PERCENT: 0,
        }
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
    is_enabled = False
    ui_log = None
    _screenshot: GrayImage = None
    _battle_list = {
        BattleListKeys.CREATURES: [],
        BattleListKeys.IS_TARGET: False
    }
    _status_bar = {
        StatusBarKeys.HP_PERCENT: 0,
        StatusBarKeys.MP_PERCENT: 0,
    }

    def __init__(self):
        self.config = read_config()

    def toggle_context_enable(self):
        self.is_enabled = not self.is_enabled

    def get_screenshot(self):
        return self._screenshot

    def set_screenshot(self, screenshot: GrayImage):
        self._screenshot = screenshot

    def save_config(self):
        with open(FILE_NAME, 'w') as config_file:
            json.dump(self.config, config_file, indent=4)

    def get_healing(self, key: HealingKeys, default=None):
        return self.config['healing'].get(key.value, default)

    def set_healing(self, key: HealingKeys, value):
        self.config['healing'][key.value] = value

    def get_status_bar(self, key: StatusBarKeys, default=None):
        return self._status_bar.get(key.value, default)

    def set_status_bar(self, key: StatusBarKeys, value):
        self._status_bar[key.value] = value

    def get_battle_list(self, key: BattleListKeys, default=None):
        return self._battle_list.get(key.value, default)

    def set_battle_list(self, key: BattleListKeys, value):
        self._battle_list[key.value] = value

    def get_cavebot_config(self, key: CavebotConfigKeys, default=None):
        return self.config['cavebot'].get(key.value, default)

    def set_cavebot_config(self, key: CavebotConfigKeys, value):
        self.config['cavebot'][key.value] = value
