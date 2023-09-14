from src.context.variables import StatusBarKeys
from src.repo.status_bar.core import get_hp_percentage, get_mp_percentage, get_follow_enabled


def set_context_status_bar_middleware(context):
    context.set_status_bar(StatusBarKeys.HP_PERCENT, get_hp_percentage(context.get_screenshot()))
    context.set_status_bar(StatusBarKeys.MP_PERCENT, get_mp_percentage(context.get_screenshot()))
    follow_enabled = get_follow_enabled(context.get_screenshot())
    context.set_status_bar(StatusBarKeys.FOLLOW_MONSTER_ENABLED, follow_enabled)
