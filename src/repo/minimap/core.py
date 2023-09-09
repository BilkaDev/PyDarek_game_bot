from typing import Optional, Any, Union

import numpy as np
from numpy import ndarray

from shared.typings import GrayImage, BBox
from src.repo.minimap.extractors import extract_minimap_image, extract_mark_to_hash
from src.repo.minimap.locates import get_zoom_minus_icon_locate, get_all_mark_pos
from src.utils import mouse
from src.utils.hash import hash_it
from src.utils.image import show

minimap_coordinates = (0, 0)


def get_minimap_coordinates(screenshot: GrayImage) -> Union[BBox, None]:
    global minimap_coordinates
    pos = get_zoom_minus_icon_locate(screenshot)
    if pos is None:
        return None
    y0 = pos[1] - 45
    x0 = pos[0] - 113
    minimap_coordinates = (x0, y0)
    return x0, y0, pos[2], pos[3]


def get_minimap_image(screenshot: GrayImage) -> Optional[ndarray[Any, Any]]:
    pos = get_minimap_coordinates(screenshot)
    if pos is None:
        return None
    return extract_minimap_image(screenshot, pos)


def click_on_minimap(x: int, y: int):
    global minimap_coordinates
    minimap_x, minimap_y = minimap_coordinates
    mouse.left_click((minimap_x + x, minimap_y + y))


# todo if hash minimap is not changed return last waypoints

def get_waypoints(screenshot: GrayImage) -> Union[list[tuple[int, int, int]], None]:
    minimap = get_minimap_image(screenshot)
    if minimap is None:
        return None
    waypoints = get_all_mark_pos(minimap, 'fight_mark')

    waypoints_with_hash = []
    for waypoint in waypoints:
        hashed_mark = get_hash_mark(minimap, (waypoint[0], waypoint[1]))
        waypoints_with_hash.append((waypoint[0], waypoint[1], hashed_mark))

    return waypoints_with_hash


def get_hash_mark(minimap, pos: tuple[int, int]):
    mark = extract_mark_to_hash(minimap, pos)

    hashed_mark = hash_it(np.ravel(mark))
    return hashed_mark
