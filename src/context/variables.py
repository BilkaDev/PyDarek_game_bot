from enum import Enum


class HealingKey(Enum):
    HP_MIN_PERCENT = "hp_min_percent"
    HP_HEAL_KEY = "hp_heal_key"
    AUTO_HEAL = "auto_heal"
    MP_MIN_PERCENT = "mp_min_percent"
    MP_HEAL_KEY = "mp_heal_key"


class StatusBarKey(Enum):
    HP_PERCENT = "hp_percent"
    MP_PERCENT = "mp_percent"
