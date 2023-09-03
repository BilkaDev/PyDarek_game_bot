import src.utils.image as im
from shared.typings import BBox, GrayImage
from src.repo.battle_list.config import size_names_wh, size_icons_wh


def get_battle_list_image(screenshot: GrayImage, battle_list_pos: BBox) -> GrayImage:
    y0 = battle_list_pos[1] + 12
    x0 = battle_list_pos[0] + 20
    return im.crop(screenshot, x0, y0, size_names_wh[0], size_names_wh[1])


def get_icon_monster_in_battle_list(screenshot: GrayImage, battle_list_pos) -> GrayImage:
    y0 = battle_list_pos[1] + 12
    x0 = battle_list_pos[0] - 2
    return im.crop(screenshot, x0, y0, size_icons_wh[0], size_icons_wh[1])
