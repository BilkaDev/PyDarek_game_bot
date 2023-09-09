from enum import Enum


class HealingKeys(Enum):
    HP_MIN_PERCENT = "hp_min_percent"
    HP_HEAL_KEY = "hp_heal_key"
    AUTO_HEAL_ENABLED = "auto_heal_enabled"
    MP_MIN_PERCENT = "mp_min_percent"
    MP_HEAL_KEY = "mp_heal_key"


class StatusBarKeys(Enum):
    HP_PERCENT = "hp_percent"
    MP_PERCENT = "mp_percent"


class BattleListKeys(Enum):
    CREATURES = 'creatures'
    IS_TARGET = 'is_target'


class CavebotConfigKeys(Enum):
    AUTO_ATTACK_ENABLED = 'auto_attack_enabled'
    MANA_TRAIN_ENABLED = 'mana_train_enabled'
    MANA_TRAIN_KEY = 'mana_train_key'
    MANA_TRAIN_MAX_PERCENT = 'mana_train_max_percent'
    CAVEBOT_ENABLED = 'cavebot_enabled'


class WaypointKeys(Enum):
    NEXT_WAYPOINT_TO_MOVE = 'next_waypoint_to_move'
    WAYPOINTS = 'waypoints'
    LAST_WAYPOINTS = 'last_waypoints'
