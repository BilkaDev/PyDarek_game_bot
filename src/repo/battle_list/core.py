import numpy as np
from numba import njit

from shared.typings import GrayImage
from src.repo.battle_list import extractors, locates
from src.repo.battle_list.config import creatures_names_images_hashes, all_creatures_images_hash
from src.utils.image import show, convert_grays_2_black, replace_values
from src.utils.hash import hash_it


def get_creatures_name(image: GrayImage) -> np.ndarray:
    black_image = convert_grays_2_black(image)
    monster_names = np.array([])
    for i in range(8, len(black_image), 22):
        # show(black_image)
        crop_image = np.ravel(black_image[i:i + 1, 0:130])
        monster_name_hashed_key = hash_it(crop_image)
        name = creatures_names_images_hashes.get(monster_name_hashed_key, None)
        if name is not None:
            monster_names = np.append(monster_names, name)
        elif monster_name_hashed_key != all_creatures_images_hash:
            monster_names = np.append(monster_names, 'All')
            break

    return monster_names


def get_is_attacking(image: GrayImage) -> bool:
    icon_pos = locates.get_battle_list_icon_position(image)
    if icon_pos is None:
        return False
    get_icon_monsters = extractors.get_icon_monster_in_battle_list(image, icon_pos)
    black_image = replace_values(get_icon_monsters, [76, 166], 192)
    is_target_line(black_image)
    return is_target_line(black_image)


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


@njit(cache=True, fastmath=True)
def is_target_line(image: np.ndarray) -> bool:
    for i in range(len(image)):
        count_white_pixel_in_line = np.count_nonzero(image[i])
        if count_white_pixel_in_line >= 18:
            return True
    return False


def recheck_is_target():
    last_is_target = False

    def check_is_target(is_target: bool):
        nonlocal last_is_target
        if not last_is_target and not is_target:
            last_is_target = False
            return False
        if is_target:
            last_is_target = True
            return True
        if not is_target:
            last_is_target = False
            return True

    return check_is_target
