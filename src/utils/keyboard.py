import pyautogui


def hot_key(*args):
    pyautogui.hotkey(*args)


def key_down(key: str):
    pyautogui.keyDown(key)


def key_up(key: str):
    pyautogui.keyUp(key)


def press(*args):
    pyautogui.press(*args)


def write(phrase: str):
    pyautogui.write(phrase)
