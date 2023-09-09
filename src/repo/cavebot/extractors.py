# old version don't support

from shared.typings import BBox, GrayImage
import numpy as np

from src.repo.cavebot.image import get_radius_mask
from src.repo.minimap.config import middle_mark_pos


def get_radius_image_around_mark(minimap: GrayImage, mark_pos: BBox, radius) -> np.ndarray:
    height, width = minimap.shape
    y0 = mark_pos[1] + middle_mark_pos[1]
    x0 = mark_pos[0] + middle_mark_pos[0]

    mask = get_radius_mask((height, width), (x0, y0), radius)

    minimap[mask == 0] = 0
    return minimap
