import src.ui.tk as ctk
from src.context.variables import CavebotConfigKeys
from src.ui.cavebot.mana_train import ManaTrain


class Cavebot:
    def __init__(self, gui):
        self.gui = gui
        self.log = gui.log
        self.context = gui.context

        ManaTrain(gui)

        self.checkbox_var, self.checkbox = ctk.create_checkbox(gui.root, text="Auto Attack")
        self.checkbox_var.set(gui.context.get_cavebot_config(CavebotConfigKeys.AUTO_ATTACK_ENABLED, False))
        self.checkbox.grid(row=gui.row, column=0, padx=10, pady=5)

        apply_button = ctk.tk.Button(gui.root, text="Apply", command=self.on_button_click)
        apply_button.grid(row=gui.row, column=1, padx=10, pady=5)
        gui.row += 1

    def on_button_click(self):
        auto_attack_enabled = self.checkbox_var.get()

        self.context.set_cavebot_config(CavebotConfigKeys.AUTO_ATTACK_ENABLED, auto_attack_enabled)

        self.context.save_config()

        if auto_attack_enabled:
            self.log.added_log("Auto attack enabled")
        else:
            self.log.added_log("Auto attack disabled")
