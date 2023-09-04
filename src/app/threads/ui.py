from threading import Thread

from src.ui.gui import Gui


class UiThread(Thread):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def run(self):
        gui = Gui(self.context)
        self.context.ui_log = gui.log
        gui.run()
