from src.context.variables import BattleListKeys
from src.repo.battle_list.core import get_creatures, get_is_attacking, recheck_is_target

recheck = recheck_is_target()


def set_context_battle_list_middleware(context):
    creatures = get_creatures(context.get_screenshot())
    is_target = get_is_attacking(context.get_screenshot())
    context.set_battle_list(BattleListKeys.CREATURES, creatures)
    context.set_battle_list(BattleListKeys.IS_TARGET, is_target)
    return context
