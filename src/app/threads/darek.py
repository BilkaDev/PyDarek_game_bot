import time

from src.app.cavebot import auto_mana_train
from src.app.healing import auto_heal_hp
from src.app.middleware.battle_list import set_context_battle_list_middleware
from src.app.middleware.screenshot import set_screenshot_middleware
from src.app.middleware.status_bar import set_context_status_bar_middleware
from src.app.targeting import auto_attack
from src.utils import get_frequency


class Darek:
    def __init__(self, context):
        self.context = context

    def mainloop(self):
        print("Darek is running")
        frequency = get_frequency()
        while True:
            start_time = time.time()
            self.handle_game_data_middleware()
            # tasks
            self.handle_game_data_tasks()
            end_time = time.time()
            diff_time = end_time - start_time
            # print(frequency())
            time.sleep(max(0.05 - diff_time, 0))

    def handle_game_data_middleware(self):
        set_screenshot_middleware(self.context)
        set_context_status_bar_middleware(self.context)
        set_context_battle_list_middleware(self.context)

    def handle_game_data_tasks(self):
        auto_heal_hp(self.context)
        auto_attack(self.context)
        auto_mana_train(self.context)
