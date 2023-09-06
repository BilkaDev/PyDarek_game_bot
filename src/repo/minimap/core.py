from shared.typings import GrayImage
from src.repo.minimap.extractors import extract_minimap_image
from src.repo.minimap.locates import get_zoom_minus_icon_locate


def get_minimap_image(screenshot: GrayImage) -> GrayImage:
    pos = get_zoom_minus_icon_locate(screenshot)
    return extract_minimap_image(screenshot, pos)
