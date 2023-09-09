import math
import time

from src.context.variables import CavebotConfigKeys, StatusBarKeys, WaypointKeys, BattleListKeys
from src.repo.minimap.config import middle_mark_pos
from src.repo.minimap.core import click_on_minimap
from src.utils import keyboard


def auto_mana_train(context):
    enabled = context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_ENABLED)
    max_percent = context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_MAX_PERCENT)
    key = context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_KEY)

    mana_percent = context.get_status_bar(StatusBarKeys.MP_PERCENT)
    if not enabled:
        return
    if mana_percent >= max_percent:
        keyboard.press(key)


entry_to_mark = True
delay = 1.5
last_time = time.time()


def auto_move_to_next_waypoint(context):
    global last_time, delay, entry_to_mark
    if context.get_battle_list(BattleListKeys.IS_TARGET):
        return
    if not context.get_cavebot_config(CavebotConfigKeys.CAVEBOT_ENABLED):
        return
    if last_time + delay > time.time():
        return
    last_time = time.time()

    waypoints = context.get_waypoint(WaypointKeys.WAYPOINTS)

    last_waypoints_hash = context.get_waypoint(WaypointKeys.LAST_WAYPOINTS)
    next_waypoint = choose_next_waypoint(waypoints, last_waypoints_hash)
    if next_waypoint is None:
        context.set_waypoint(WaypointKeys.LAST_WAYPOINTS, [])
        return
    x, y, hashed = next_waypoint
    center_x = x + middle_mark_pos[0]
    center_y = y + middle_mark_pos[1]

    click_on_minimap(x + middle_mark_pos[0], y + middle_mark_pos[1])

    if 48 <= center_x <= 52 and 48 <= center_y <= 52:
        entry_to_mark = False
        if hashed in last_waypoints_hash:
            return
        new_last_waypoints_hash = append_hashed(last_waypoints_hash, hashed)
        context.set_waypoint(WaypointKeys.LAST_WAYPOINTS, new_last_waypoints_hash)


def choose_next_waypoint(waypoints, last_waypoints_hash):
    global entry_to_mark
    center = (50, 50)

    closest_point = None
    closest_distance = float('inf')

    for waypoint in waypoints:
        x2, y2, _ = waypoint
        center_x2 = x2 + middle_mark_pos[0]
        center_y2 = y2 + middle_mark_pos[1]

        distance = math.sqrt((center_x2 - center[0]) ** 2 + (center_y2 - center[1]) ** 2)
        if entry_to_mark and distance <= 12:
            return waypoint
        if not entry_to_mark and distance <= 12:
            continue

        if waypoint[2] in last_waypoints_hash:
            continue

        if distance < closest_distance:
            closest_distance = distance
            closest_point = waypoint
            if distance <= 15:
                entry_to_mark = True
    return closest_point


def append_hashed(list_hash, hashed: int):
    if len(list_hash) > 4:
        list_hash.append(hashed)
        return list_hash[:1]
    else:
        list_hash.append(hashed)
        return list_hash
