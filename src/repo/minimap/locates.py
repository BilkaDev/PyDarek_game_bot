from typing import Union
from shared.typings import BBox, GrayImage
from src.repo.minimap.config import images
from src.utils.hash import cache_object_position
from src.utils.vision import locate, locate_multiple


@cache_object_position
def get_zoom_minus_icon_locate(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['zoom_minus_icon'])


@cache_object_position
def get_mark_pos(screenshot: GrayImage, mark: str) -> Union[BBox, None]:
    return locate(screenshot, images[mark])


def get_all_mark_pos(screenshot: GrayImage, mark: str) -> list[BBox]:
    return locate_multiple(screenshot, images[mark])
