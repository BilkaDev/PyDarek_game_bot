from src.context.variables import StatusBarKeys, HealingKeys
from src.utils import keyboard


def auto_heal_hp(context):
    if not context.get_healing(HealingKeys.AUTO_HEAL_ENABLED):
        return
    min_hp_percent = context.get_healing(HealingKeys.HP_MIN_PERCENT)
    key = context.get_healing(HealingKeys.HP_HEAL_KEY)
    hp_percent = context.get_status_bar(StatusBarKeys.HP_PERCENT)
    if hp_percent <= min_hp_percent:
        context.set_status_bar(StatusBarKeys.HP_PERCENT, hp_percent)
        keyboard.press(key)
