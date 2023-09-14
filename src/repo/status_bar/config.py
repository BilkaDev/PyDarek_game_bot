import pathlib
import src.utils.image as im
import numpy as np

from src.utils.hash import hash_it

dir_path = pathlib.Path(__file__).parent.resolve()
icons_path = f'{dir_path}/images'
images = {
    'hp': im.load_RGB2Gray(f'{icons_path}/status-bar_hp.png'),
    'mp': im.load_RGB2Gray(f'{icons_path}/status-bar_mp.png'),
    'pvp_button': im.load_RGB2Gray(f'{icons_path}/pvp_button.png'),
    'follow_monster_button': im.load_RGB2Gray(f'{icons_path}/follow_monster_button.png')
}
hp_bar_allowed_pixels_colors = np.array([113, 121, 129, 140, 155])
bar_size = 92
mana_bar_allowed_pixels_colors = np.array([101, 107, 115, 126, 130])

hashed_follow_monster_button = np.ravel(images['follow_monster_button'][10:11, 0:20])
hashed_follow_monster_button = hash_it(hashed_follow_monster_button)
