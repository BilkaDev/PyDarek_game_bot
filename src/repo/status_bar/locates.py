from typing import Union
from shared.typings import BBox, GrayImage
from src.repo.status_bar.config import images
from src.utils.vision import locate
from src.utils.hash import cache_object_position


@cache_object_position
def get_hp_icon_position(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['hp'])


@cache_object_position
def get_mp_icon_position(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['mp'])


@cache_object_position
def get_pvp_button_position(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['pvp_button'])
