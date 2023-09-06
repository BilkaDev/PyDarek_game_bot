import src.utils.image as im
from shared.typings import BBox, GrayImage
from src.repo.minimap.config import minimap_size_wh


def extract_minimap_image(screenshot: GrayImage, minus_icon_pos: BBox) -> GrayImage:
    y0 = minus_icon_pos[1] - 45
    x0 = minus_icon_pos[0] - 113
    return im.crop(screenshot, x0, y0, minimap_size_wh[0], minimap_size_wh[1])
