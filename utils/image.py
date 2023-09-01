import cv2
from numba import njit
import numpy as np
from typings import GrayImage

def show(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

@njit(cache=True, fastmath=True)
def convert_grays_2_black(arr: np.ndarray) -> np.ndarray:
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i, j] >= 50 and arr[i, j] <= 100:
                arr[i, j] = 0
    return arr

def RGB2Gray(image: np.ndarray) -> GrayImage:
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def load_RGB2Gray(path: str) -> GrayImage:
    return np.array(RGBtoGray(load(path)), dtype=np.uint8)


def save(arr, name: str):
    im = Image.fromarray(arr)
    im.save(name)

def crop(image: GrayImage, x: int, y: int, width: int, height: int) -> GrayImage:
    return image[y:y + height, x:x + width]

def load(path: str) -> np.ndarray:
    return np.array(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB), dtype=np.uint8)