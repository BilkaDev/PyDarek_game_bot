from src.context.variables import StatusBarKey, HealingKey
from src.utils import keyboard


def auto_heal_hp(context):
    min_hp_percent = context.get_healing(HealingKey.HP_MIN_PERCENT)
    key = context.get_healing(HealingKey.HP_HEAL_KEY)
    hp_percent = context.get_status_bar(StatusBarKey.HP_PERCENT)

    if hp_percent <= min_hp_percent:
        context.set_status_bar(StatusBarKey.HP_PERCENT, hp_percent)
        keyboard.press(key)
