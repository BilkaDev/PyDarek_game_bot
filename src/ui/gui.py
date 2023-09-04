import src.ui.tk as ctk
from src.ui.auto_heal import AutoHeal
from src.ui.cavebot.cavebot import Cavebot
from src.ui.log import Log


class Gui:
    def __init__(self, context):
        self.context = context
        self.root = ctk.tk.Tk()
        self.root.title("PyDarek")
        self.root.geometry("500x500")
        self.log = Log(self)
        self.row = 0

        AutoHeal(self)
        Cavebot(self)
        self._start_off_button()

    def _start_off_button(self):
        self._text_start_off_button = ctk.tk.StringVar()
        self._text_start_off_button.set("Start")
        text = f'{"Start" if self.context.is_enabled else "Stop"}(CTRL+1)'
        element = ctk.tk.Button(self.root, textvariable=self._text_start_off_button,
                                command=self._toggle_button)
        element.grid(row=self.row, column=1, padx=5, pady=10)
        self.row += 1

    def _toggle_button(self):
        self.context.toggle_context_enable()
        self._text_start_off_button.set("Stop(CTRL+1)" if self.context.is_enabled else "Start")

    def run(self):
        self.root.mainloop()
