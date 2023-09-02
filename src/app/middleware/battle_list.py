from src.context.variables import BattleListKey
from src.repo.battle_list.core import get_creatures


def set_context_battle_list_middleware(context):
    creatures = get_creatures(context.get_screenshot())
    context.set_battle_list(BattleListKey.CREATURES, creatures)
    return context
