from src.app.threads.darek import Darek
from src.app.threads.ui import UiThread
from src.context.context import Context


def main():
    context = Context()
    ui_thread = UiThread(context)
    ui_thread.start()
    darek = Darek(context)
    darek.mainloop()


if __name__ == "__main__":
    main()
