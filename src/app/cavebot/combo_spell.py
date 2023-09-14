import time

from src.context.variables import BattleListKeys, CavebotConfigKeys
from src.utils import keyboard

spell_cooldown = 2
ico_hur_cooldown = 4
exori_cooldown = 5

last_time_use_spell = time.time()
last_time_use_hur = time.time()
last_time_use_ico = time.time()
last_time_use_exori = time.time()


def combo_spell(context):
    global last_time_use_spell, last_time_use_ico, last_time_use_exori, last_time_use_hur, spell_cooldown, ico_hur_cooldown, exori_cooldown
    is_target = context.get_battle_list(BattleListKeys.IS_TARGET)
    count_monsters = len(context.get_battle_list(BattleListKeys.CREATURES))
    if not context.get_cavebot_config(CavebotConfigKeys.AUTO_ATTACK_ENABLED):
        return
    if is_target:
        # exori ico
        if check_cooldown(spell_cooldown, last_time_use_spell) and check_cooldown(ico_hur_cooldown, last_time_use_hur):
            last_time_use_spell = time.time()
            last_time_use_hur = time.time()
            keyboard.press('4')
        # exori
        if count_monsters >= 2 and check_cooldown(spell_cooldown, last_time_use_spell) and check_cooldown(
                exori_cooldown, last_time_use_exori):
            last_time_use_spell = time.time()
            last_time_use_exori = time.time()
            keyboard.press('5')
        # exori hur
        if check_cooldown(spell_cooldown, last_time_use_spell) and check_cooldown(ico_hur_cooldown, last_time_use_ico):
            last_time_use_spell = time.time()
            last_time_use_hur = time.time()
            keyboard.press('6') 

def check_cooldown(cooldown_time, last_time_use):
    if last_time_use + cooldown_time >= time.time():
        return False
    else:
        return True
