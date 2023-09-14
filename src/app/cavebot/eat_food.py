import time

from src.context.variables import CavebotConfigKeys
from src.utils import keyboard

food_time = time.time()
delay_time = 60


def auto_eat_food(context):
    global food_time, delay_time
    key = context.get_cavebot_config(CavebotConfigKeys.FOOD_KEY)
    if not context.get_cavebot_config(CavebotConfigKeys.FOOD_ENABLED):
        return

    if food_time + delay_time < time.time():
        keyboard.press(key)
        food_time = time.time()
