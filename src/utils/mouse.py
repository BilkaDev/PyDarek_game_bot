import pyautogui


def left_click(coordinate_xy=None):
    if coordinate_xy is None:
        pyautogui.leftClick()
        return
    pyautogui.leftClick(coordinate_xy[0], coordinate_xy[1])
