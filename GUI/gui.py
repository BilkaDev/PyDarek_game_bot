import GUI.tk as ctk
from GUI.auto_heal import AutoHeal
from GUI.log import Log

class Gui:
    def __init__(self, context):
        self.context = context
        self.root = ctk.tk.Tk()
        self.root.title("Darek")
        self.root.geometry("500x500")
        self.log = Log(self.root)

        AutoHeal(self)
    
    def run(self):
        self.root.mainloop()
    