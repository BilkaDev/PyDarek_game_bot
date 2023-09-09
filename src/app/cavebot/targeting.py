from src.context.variables import BattleListKeys, CavebotConfigKeys
from src.utils import keyboard


def auto_attack(context):
    if not context.get_cavebot_config(CavebotConfigKeys.AUTO_ATTACK_ENABLED):
        return
    if context.get_battle_list(BattleListKeys.IS_TARGET):
        return
    if len(context.get_battle_list(BattleListKeys.CREATURES)) > 0:
        context.set_battle_list(BattleListKeys.IS_TARGET, True)
        keyboard.press('space')
