from src.utils.screenshot import get_screenshot


def set_screenshot_middleware(context):
    screenshot = get_screenshot()
    context.set_screenshot(screenshot)
    return context
