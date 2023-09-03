import pathlib
import src.utils.image as im
import numpy as np
from src.utils.hash import hash_it
from wiki.monsters import creatures

dir_path = pathlib.Path(__file__).parent.resolve()
icons_path = f'{dir_path}/images'
monsters_path = f'{dir_path}/images/monsters'
images = {
    'battle_list_icon': im.load_RGB2Gray(f'{icons_path}/battle-list-icon.png'),
}
size_names_wh = (130, 200)
size_icons_wh = (22, 200)

creatures_names_images_hashes = {}


for creature_name in creatures:
    """
    In this method, we create a hash of the image of the creature name.
    Then, we store the hash in a dictionary.
    
    monster_images have to be 12x130 pixels.
    """
    creature_name_image = im.load_RGB2Gray(
        f'{monsters_path}/{creature_name}.png')
    creature_name_image = np.ravel(creature_name_image[6:7, 0:130])
    creature_name_image_hash = hash_it(creature_name_image)
    creatures_names_images_hashes[creature_name_image_hash] = creature_name

all_creatures_images_hash = creature_name_image = im.load_RGB2Gray(
    f'{monsters_path}/All.png')
all_creatures_images_hash = np.ravel(all_creatures_images_hash[6:7, 0:130])
all_creatures_images_hash = hash_it(all_creatures_images_hash)
