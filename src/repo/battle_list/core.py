import numpy as np
from numba import njit

from shared.typings import GrayImage
from src.repo.battle_list import extractors, locates
from src.repo.battle_list.config import creatures_names_images_hashes, all_creatures_images_hash
from src.utils.image import show, convert_grays_2_black
from src.utils.hash import hash_it


def get_creatures_name(image: GrayImage) -> np.ndarray:
    black_image = convert_grays_2_black(image)
    monster_names = np.array([])
    for i in range(8, len(black_image), 22):
        crop_image = np.ravel(black_image[i:i + 1, 0:130])
        monster_name_hashed_key = hash_it(crop_image)
        name = creatures_names_images_hashes.get(monster_name_hashed_key, None)
        if name is not None:
            monster_names = np.append(monster_names, name)
        elif monster_name_hashed_key != all_creatures_images_hash:
            monster_names = np.append(monster_names, 'All')
            break

    return monster_names


def get_creatures(image: GrayImage) -> np.ndarray:
    """
    Returns array with creatures in battle list.

    :param image: The image.
    :return: The array of the creatures.
    """
    icon_pos = locates.get_battle_list_icon_position(image)
    if icon_pos is None:
        return np.array([], dtype=str)
    list_image = extractors.get_battle_list_image(image, icon_pos)
    return get_creatures_name(list_image)
