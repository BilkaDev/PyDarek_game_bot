import src.utils.image as im
from shared.typings import BBox, GrayImage
from src.repo.battle_list.config import size_wh


def get_battle_list_image(screenshot: GrayImage, battle_list_pos: BBox) -> GrayImage:
    y0 = battle_list_pos[1] + 12
    x0 = battle_list_pos[0] + 20
    return im.crop(screenshot, x0, y0, size_wh[0], size_wh[1])
