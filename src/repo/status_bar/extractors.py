import src.utils.image as im
from shared.typings import BBox, GrayImage
from src.repo.status_bar.config import bar_size


def get_hp_bar(screenshot: GrayImage, heart_pos: BBox) -> GrayImage:
    y0 = heart_pos[1] + 5
    width = bar_size
    height = 3
    x0 = heart_pos[0] + 14
    return im.crop(screenshot, x0, y0, width, height)


def get_mp_bar(screenshot: GrayImage, mana_pos: BBox) -> GrayImage:
    y0 = mana_pos[1] + 5
    width = bar_size
    height = 3
    x0 = mana_pos[0] + 15
    return im.crop(screenshot, x0, y0, width, height)
