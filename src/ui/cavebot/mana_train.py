import src.ui.tk as ctk
from src.context.variables import CavebotConfigKeys


class ManaTrain:
    def __init__(self, gui):
        self.gui = gui
        self.row = gui.row
        self.log = gui.log
        self.context = gui.context

        self.mana_entry, self.checkbox_var, self.checkbox = ctk.create_row(gui.root, row=gui.row, text="Max Mp%",
                                                                           checkbox_text="Mana Train")

        self.mana_entry.insert(0, gui.context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_MAX_PERCENT, 0))
        self.checkbox_var.set(gui.context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_ENABLED, False))

        self.mana_key_entry = ctk.create_row(gui.root, row=gui.row + 1, text="Key:")
        self.mana_key_entry.insert(0, gui.context.get_cavebot_config(CavebotConfigKeys.MANA_TRAIN_KEY, ''))

        apply_button = ctk.tk.Button(gui.root, text="Apply", command=self.on_button_click)
        apply_button.grid(row=gui.row + 1, column=2, padx=10, pady=5)
        gui.row += 2

    def on_button_click(self):
        mana_train_enabled = self.checkbox_var.get()
        mana_amount = float(self.mana_entry.get())
        key = self.mana_key_entry.get()

        self.context.set_cavebot_config(CavebotConfigKeys.MANA_TRAIN_ENABLED, mana_train_enabled)
        self.context.set_cavebot_config(CavebotConfigKeys.MANA_TRAIN_MAX_PERCENT, mana_amount)
        self.context.set_cavebot_config(CavebotConfigKeys.MANA_TRAIN_KEY, key)

        self.context.save_config()

        if mana_train_enabled:
            self.log.added_log("Mana train enabled")
        else:
            self.log.added_log("Mana train disabled")
