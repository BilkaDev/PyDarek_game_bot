# old version of waypoint don't support it
import cv2
import numpy as np


def get_radius_mask(shape: tuple, center: tuple, radius: int) -> np.ndarray:
    height, width = shape
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(mask, center, radius, (255, 255, 255), -1)
    return mask


def center_mark(image, pos):
    height, width = image.shape
    dx = (width // 2) - pos[0]
    dy = (height // 2) - pos[1]

    M = np.float32([[1, 0, dx], [0, 1, dy]])
    image_shifted = cv2.warpAffine(image, M, (width, height))
    return image_shifted


def decenter_mark(image, pos):
    height, width = image.shape
    dx = pos[0] - (width // 2)
    dy = pos[1] - (height // 2)
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    image_shifted = cv2.warpAffine(image, M, (width, height))
    return image_shifted
