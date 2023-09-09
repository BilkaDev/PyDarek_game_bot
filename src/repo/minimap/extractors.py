import src.utils.image as im
from shared.typings import BBox, GrayImage
from src.repo.minimap.config import minimap_size_wh


def extract_minimap_image(screenshot: GrayImage, minus_icon_pos: BBox) -> GrayImage:
    return im.crop(screenshot, minus_icon_pos[0], minus_icon_pos[1], minimap_size_wh[0], minimap_size_wh[1])


def extract_mark_to_hash(minimap: GrayImage, pos: tuple[int, int]):
    return im.crop(minimap, pos[0] - 2, pos[1] - 3, 13, 13)
