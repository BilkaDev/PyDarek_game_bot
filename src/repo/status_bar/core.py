from numba import njit
from shared.typings import GrayImage
from src.repo.status_bar import extractors, locates
from src.repo.status_bar.config import hp_bar_allowed_pixels_colors, mana_bar_allowed_pixels_colors, \
    hashed_follow_monster_button
from src.repo.status_bar.extractors import get_follow_monster_button
from src.repo.status_bar.locates import get_pvp_button_position
from src.utils import mouse
from src.utils.hash import hash_it
from src.utils.image import show


def get_hp_percentage(image: GrayImage) -> float:
    """
    Returns the HP percentage of an image.

    :param image: The image.
    :return: The HP percentage of the image.
    """
    heart_pos = locates.get_hp_icon_position(image)
    if heart_pos is None:
        return 0
    bar = extractors.get_hp_bar(image, heart_pos)
    count = get_percentage_bar(bar, 'hp')
    return count


@njit(cache=True, fastmath=True)
def get_percentage_bar(image, type_bar) -> float:
    middle_bar = image[1]
    allowed_pixels = hp_bar_allowed_pixels_colors if type_bar == 'hp' else mana_bar_allowed_pixels_colors
    count = 0
    for i in range(len(middle_bar)):
        count += 1 if middle_bar[i] in allowed_pixels else 0
    return count / len(middle_bar)


def get_mp_percentage(image: GrayImage) -> float:
    """
    Returns the MP percentage of an image.

    :param image: The image in Gray colors.
    :return: The MP percentage of the image.
    """
    mana_pos = locates.get_mp_icon_position(image)
    if mana_pos is None:
        return 0
    bar = extractors.get_mp_bar(image, mana_pos)
    count = get_percentage_bar(bar, 'mana')
    return count


def get_follow_enabled(image: GrayImage) -> bool:
    pos = get_pvp_button_position(image)
    follow_button = get_follow_monster_button(image, pos)
    hash_button = hash_it(follow_button[10:11, 0:20])
    return hash_button != hashed_follow_monster_button


def press_follow_button(image: GrayImage):
    pos = get_pvp_button_position(image)
    x = pos[0]
    y = pos[1]
    mouse.left_click((x + 10 + 22, y + 10 - 49))
