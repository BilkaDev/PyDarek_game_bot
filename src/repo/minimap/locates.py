from typing import Union
from shared.typings import BBox, GrayImage
from src.repo.minimap.config import images
from src.utils.hash import cache_object_position
from src.utils.vision import locate


@cache_object_position
def get_zoom_minus_icon_locate(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['zoom_minus_icon'])
