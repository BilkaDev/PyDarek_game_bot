import time

from src.app.cavebot.cavebot import auto_mana_train, auto_move_to_next_waypoint
from src.app.cavebot.combo_spell import combo_spell
from src.app.healing import auto_heal_hp
from src.app.middleware.battle_list import set_context_battle_list_middleware
from src.app.middleware.screenshot import set_context_screenshot_middleware
from src.app.middleware.status_bar import set_context_status_bar_middleware
from src.app.cavebot.targeting import auto_attack
from src.app.middleware.waypoint import set_context_waypoint_middleware
from src.app.cavebot.eat_food import auto_eat_food
from src.context.variables import StatusBarKeys
from src.repo.status_bar.core import press_follow_button
from src.utils import get_frequency


class Darek:
    def __init__(self, context):
        self.context = context

    def mainloop(self):

        print("Darek is running")
        frequency = get_frequency()
        while True:
            start_time = time.time()
            if not self.context.is_enabled:
                time.sleep(0.05)
                continue
            try:
                self.handle_game_data_middleware()
            # tasks
            except TypeError as e:
                print(e)
                self.context.ui_log.added_error("Please open Tibia and open windows battle list and skills")
                self.context.toggle_context_enable()
                continue
            if not self.context.is_enabled:
                continue
            self.handle_game_data_tasks()
            end_time = time.time()
            diff_time = end_time - start_time
            # print(frequency())
            time.sleep(max(0.05 - diff_time, 0))

    def handle_game_data_middleware(self):
        set_context_screenshot_middleware(self.context)
        set_context_status_bar_middleware(self.context)
        set_context_battle_list_middleware(self.context)
        set_context_waypoint_middleware(self.context)

    def handle_game_data_tasks(self):
        auto_heal_hp(self.context)
        auto_attack(self.context)
        combo_spell(self.context)
        auto_mana_train(self.context)
        auto_move_to_next_waypoint(self.context)
        if not self.context.get_status_bar(StatusBarKeys.FOLLOW_MONSTER_ENABLED):
            press_follow_button(self.context.get_screenshot())
        auto_eat_food(self.context)
