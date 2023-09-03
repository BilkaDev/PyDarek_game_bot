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
        self.log = Log(self.root)
        self.row = 0

        AutoHeal(self)
        Cavebot(self)

    def run(self):
        self.root.mainloop()
