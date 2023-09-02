from typing import Union
from shared.typings import BBox, GrayImage
from src.repo.battle_list.config import images
from src.utils.vision import locate
from src.utils.hash import cache_object_position


@cache_object_position
def get_battle_list_icon_position(screenshot: GrayImage) -> Union[BBox, None]:
    return locate(screenshot, images['battle_list_icon'])
