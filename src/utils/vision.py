from typing import Union
from shared.typings import BBox, GrayImage
import numpy as np
import cv2


def locate(compare_image: GrayImage, img: GrayImage, confidence: float = 0.85) -> Union[BBox, None]:
    match = cv2.matchTemplate(compare_image, img, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    if res[1] <= confidence:
        return None
    return res[3][0], res[3][1], len(img[0]), len(img)


def locate_multiple(compare_image: GrayImage, img: GrayImage, confidence: float = 0.85) -> list[BBox]:
    match = cv2.matchTemplate(compare_image, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(match >= confidence)
    result_list = []
    for pt in zip(*loc[::-1]):
        result_list.append((pt[0], pt[1], len(compare_image[0]), len(compare_image)))
    return result_list
