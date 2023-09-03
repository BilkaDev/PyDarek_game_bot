import mss
import numpy as np
import cv2

latest_screenshot = None
camera = mss.mss()
monitors = camera.monitors
monitor = monitors[-1]

for monitorKey in monitors:
    if monitorKey['left'] == 0 and monitorKey['top'] == 0 and monitorKey['width'] == 1920 and monitorKey[
        'height'] == 1080:
        monitor = monitorKey
        break


def get_screenshot():
    global camera, latest_screenshot, monitor
    screenshot = camera.grab(monitor)

    screenshot_np = np.array(screenshot)

    screenshot_without_alpha = screenshot_np[:, :, 0:3]
    if screenshot is None:
        return latest_screenshot
    latest_screenshot = cv2.cvtColor(screenshot_without_alpha, cv2.COLOR_BGR2GRAY)

    return latest_screenshot
