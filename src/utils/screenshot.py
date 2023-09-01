import mss
import numpy as np
import cv2

latest_screenshot = None
camera = mss.mss()
monitor = camera.monitors[-1]


def get_screenshot():
    global camera, latest_screenshot, monitor
    screenshot = camera.grab(monitor)
    screenshot_np = np.array(screenshot)

    if screenshot is None:
        return latest_screenshot
    latest_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGRA2GRAY)
    return latest_screenshot
