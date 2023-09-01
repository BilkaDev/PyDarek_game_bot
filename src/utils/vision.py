from typing import Union
from shared.typings import BBox, GrayImage
import cv2


def locate(compareImage: GrayImage, img: GrayImage, confidence: float = 0.85) -> Union[BBox, None]:
    match = cv2.matchTemplate(compareImage, img, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    if res[1] <= confidence:
        return None
    return res[3][0], res[3][1], len(img[0]), len(img)


def locateMultiple(compareImg: GrayImage, img: GrayImage, confidence: float = 0.85) -> Union[BBox, None]:
    match = cv2.matchTemplate(compareImg, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(match >= confidence)
    resultList = []
    for pt in zip(*loc[::-1]):
        resultList.append((pt[0], pt[1], len(compareImg[0]), len(compareImg)))
    return resultList
