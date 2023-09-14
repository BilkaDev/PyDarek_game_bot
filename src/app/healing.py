import time

from src.context.variables import StatusBarKeys, HealingKeys
from src.utils import keyboard

spell_cooldown = 1
potion_cooldown = 1
buff_cooldown = 60

last_time_use_spell = time.time()
last_time_use_potion = time.time()
last_time_use_buff = time.time()


def auto_heal_hp(context):
    global last_time_use_spell, last_time_use_potion, last_time_use_buff
    mp_percent = context.get_status_bar(StatusBarKeys.MP_PERCENT)
    if not context.get_healing(HealingKeys.AUTO_HEAL_ENABLED):
        return
    min_hp_percent = context.get_healing(HealingKeys.HP_MIN_PERCENT)
    key = context.get_healing(HealingKeys.HP_HEAL_KEY)
    hp_percent = context.get_status_bar(StatusBarKeys.HP_PERCENT)
    # for spell
    if hp_percent <= min_hp_percent:
        if check_cooldown(spell_cooldown, last_time_use_spell):
            last_time_use_spell = time.time()
            keyboard.press(key)
    # for potions
    if hp_percent <= 0.60:
        if check_cooldown(potion_cooldown, last_time_use_potion):
            last_time_use_potion = time.time()
            keyboard.press('2')
    # for buff
    if check_cooldown(buff_cooldown, last_time_use_buff):
        last_time_use_buff = time.time()
        keyboard.press('0')
    if mp_percent <= 0.50:
        if check_cooldown(potion_cooldown, last_time_use_potion):
            last_time_use_potion = time.time()
            keyboard.press('3')


def check_cooldown(cooldown_time, last_time_use):
    if last_time_use + cooldown_time >= time.time():
        return False
    else:
        return True
