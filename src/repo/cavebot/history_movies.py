# old version waypoint doesn't support'

from shared.typings import GrayImage, BBox
from src.repo.cavebot.config import radius, middle_mark_px
from src.repo.cavebot.core import get_distance_from_mark
from src.repo.cavebot.image import get_radius_mask, center_mark, decenter_mark


class HistoryMoves:
    def __init__(self):
        self.moves_radius = None
        self.clear_history()
        self.minimap = None

    def clear_history(self):
        self.moves_radius = get_radius_mask((radius * 2, radius * 2), (50, 50), radius)

    def set_history(self, minimap: GrayImage, finish_mark_pos: BBox):
        center_pos_mark_x = finish_mark_pos[0] + middle_mark_px
        center_pos_mark_y = finish_mark_pos[1] + middle_mark_px

        x, y = get_distance_from_mark(minimap, finish_mark_pos, )
        centered_mark = center_mark(minimap, (center_pos_mark_x, center_pos_mark_y))

        # window game for zoom-1
        height, width = window_game_size = (11, 15)
        height = height // 2
        width = width // 2
        self.moves_radius[50 - height - 1 + y: 50 + height + y, 50 - width - 1 + x: 50 + width + x] = 0
        centered_mark[self.moves_radius == 0] = 0
        center_minimap = decenter_mark(centered_mark,
                                       (finish_mark_pos[0] + middle_mark_px, finish_mark_pos[1] + middle_mark_px))
        self.minimap = center_minimap
        return center_minimap




def find_shortest_path(matrix):
    height, width = matrix.shape
    window_height, window_width = window_game_size
    window_height = window_height // 2
    window_width = window_width // 2

    center_x = width // 2
    center_y = height // 2
    # print(matrix[50, 50 - window_width - 2])  # w lewo
    # print(matrix[50, 50 + window_width])  # w prawo sa to indexy +1 poza widok gracza
    # print(matrix[50 + window_height, 50])  # w dół sa to indexy +1 poza widok gracza
    # print(matrix[50 - window_height - 1, 50])  # w gore sa to indexy +1 poza widok gracza
    left_side_x = 50 - window_width - 2
    right_side_x = 50 + window_width
    top_side_y = 50 - window_height - 2
    bottom_side_y = 50 + window_height
    print(top_side_y)
    if check_x_side(matrix, left_side_x):
        print("is left side")
    if check_x_side(matrix, right_side_x):
        print("is right side")
    if check_y_side(matrix, bottom_side_y):
        print("is bottom side")
    if check_y_side(matrix, top_side_y):
        print("is top side")


def check_x_side(array: np.ndarray, x: int, ):
    for i in range(45, 55):
        if array[i, x] == 255:
            return True


def check_y_side(array: np.ndarray, y: int, ):
    for i in range(42, 57):
        if array[y, i] == 255:
            return True