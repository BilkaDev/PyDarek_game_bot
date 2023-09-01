import pathlib
import src.utils.image as im
import numpy as np

dir_path = pathlib.Path(__file__).parent.resolve()
icons_path = f'{dir_path}/images'
images = {
    'hp': im.load_RGB2Gray(f'{icons_path}/status-bar_hp.png'),
    'mp': im.load_RGB2Gray(f'{icons_path}/status-bar_mp.png')
}
hp_bar_allowed_pixels_colors = np.array([79, 118, 121, 110, 62])
bar_size = 94
mana_bar_allowed_pixels_colors = np.array([68, 95, 97, 89, 52])