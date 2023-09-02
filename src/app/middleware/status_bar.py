from src.context.variables import StatusBarKey
from src.repo.status_bar.core import get_hp_percentage, get_mp_percentage


def set_context_status_bar_middleware(context):
    context.set_status_bar(StatusBarKey.HP_PERCENT, get_hp_percentage(context.get_screenshot()))
    context.set_status_bar(StatusBarKey.MP_PERCENT, get_mp_percentage(context.get_screenshot()))
