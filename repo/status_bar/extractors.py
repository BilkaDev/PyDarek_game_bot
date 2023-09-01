from typings import BBox,GrayImage
from .config import bar_size

def get_hp_bar(screenshot: GrayImage,heart_pos: BBox) -> GrayImage:
    y0 = heart_pos[1] + 5
    y1 = y0 + 1
    x0 = heart_pos[0] + 13
    x1 = x0 + bar_size
