from src.context.variables import CavebotConfigKeys, StatusBarKeys
from src.utils import keyboard


def auto_mana_train(context):
    enabled = context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_ENABLED)
    max_percent = context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_MAX_PERCENT)
    key = context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_KEY)

    mana_percent = context.get_status_bar(StatusBarKeys.MP_PERCENT)
    if not enabled:
        return
    if mana_percent >= max_percent:
        keyboard.press(key)