import src.ui.tk as ctk
from src.context.variables import HealingKeys


class AutoHeal:
    def __init__(self, gui):
        self.gui = gui
        self.log = gui.log
        self.context = gui.context

        self.heal_entry, self.checkbox_var, self.checkbox = ctk.create_row(gui.root, row=gui.row, text="Min HP%",
                                                                           checkbox_text="Auto Heal")

        self.heal_entry.insert(0, gui.context.get_healing(HealingKeys.HP_MIN_PERCENT))
        self.checkbox_var.set(gui.context.get_healing(HealingKeys.AUTO_HEAL_ENABLED, False))

        self.heal_key_entry = ctk.create_row(gui.root, row=gui.row + 1, text="Key:")
        self.heal_key_entry.insert(0, gui.context.get_healing(HealingKeys.HP_HEAL_KEY, ''))

        apply_button = ctk.tk.Button(gui.root, text="Apply", command=self.on_button_click)
        apply_button.grid(row=gui.row + 1, column=2, padx=10, pady=5)
        gui.row += 2

    def on_button_click(self):
        heal_enabled = self.checkbox_var.get()
        heal_amount = float(self.heal_entry.get())
        heal_key = self.heal_key_entry.get()

        self.context.set_healing(HealingKeys.AUTO_HEAL_ENABLED, heal_enabled)
        self.context.set_healing(HealingKeys.HP_MIN_PERCENT, heal_amount)
        self.context.set_healing(HealingKeys.HP_HEAL_KEY, heal_key)

        self.context.save_config()

        if heal_enabled:
            self.log.added_log("Auto Heal enabled")
        else:
            self.log.added_log("Auto heal disabled")
