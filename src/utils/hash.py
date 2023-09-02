import xxhash
import numpy as np


def hash_it(arr: np.ndarray) -> int:
    return xxhash.xxh64(np.ascontiguousarray(arr), seed=20220605).intdigest()


def cache_object_position(func):
    last_x = None
    last_y = None
    last_w = None
    last_h = None
    last_img_hash = None

    def inner(screenshot):
        nonlocal last_x, last_y, last_w, last_h, last_img_hash
        if last_x is not None and last_y is not None and last_w is not None and last_h is not None:
            if hash_it(screenshot[last_y:last_y + last_h, last_x:last_x + last_w]) == last_img_hash:
                return last_x, last_y, last_w, last_h
        res = func(screenshot)

        if res is None:
            return None

        last_x = res[0]
        last_y = res[1]
        last_w = res[2]
        last_h = res[3]

        last_img_hash = hash_it(
            screenshot[last_y:last_y + last_h, last_x:last_x + last_w])
        return res

    return inner
