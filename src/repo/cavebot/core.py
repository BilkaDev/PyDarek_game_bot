from typing import Union

import numpy as np

from shared.typings import GrayImage, BBox
from src.repo.cavebot.extractors import get_radius_image_around_mark, get_radius_mask
from src.repo.cavebot.image import decenter_mark, center_mark
from src.repo.minimap.config import available_colors_to_move, hero_pos, middle_mark_pos
from src.repo.minimap.core import get_minimap_image
import src.utils.image as im

# zapisuje w tablicy gdzie juz byl oblicza dystan postaci od srodka mamy czyli swojej pozycji i od marka

# gdy dojdzie do braku dostepnych pol kasuje tablice lub jesli jest check pointer to kasuje tablice i do niego idzie ....
# ustawienie mapy maksymalnie  - i raz + zrobic do tego w minimap funkcje click zoom plus ...


history = get_radius_mask((100, 100), (50, 50), radius = 50)


def get_minimap_with_fields_to_move(minimap: GrayImage) -> Union[np.ndarray, None]:
    minimap_with_fields_to_move = im.replace_values(minimap, available_colors_to_move, 255)
    return minimap_with_fields_to_move


def get_distance_from_mark(minimap: GrayImage, finish_mark_pos: BBox) -> tuple:
    hero_poz_y = hero_pos[0]
    hero_poz_x = hero_pos[1]
    mark_pos_y = finish_mark_pos[1] + middle_mark_pos[1]
    mark_pos_x = finish_mark_pos[0] + middle_mark_pos[0]
    return hero_poz_x - mark_pos_x, hero_poz_y - mark_pos_y
