from config import images
from typing import Union
from shared.typings import BBox, GrayImage
from src.utils.vision import locate


def get_hp_icon_position(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['hp'])


def get_mp_icon_position(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['mp'])
