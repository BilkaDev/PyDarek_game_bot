import pathlib
import src.utils.image as im

dir_path = pathlib.Path(__file__).parent.resolve()
images_path = f'{dir_path}/images'
mark_path = f'{images_path}/marks/'

icon_zoom_minus_path = f'{images_path}/zoom_minus.png'
icon_zoom_plus_path = f'{images_path}/zoom_plus.png'
finish_mark_path = f'{mark_path}/cavebot_finish_mark.png'
up_mark_path = f'{mark_path}/cavebot_up_mark.png'
down_mark_path = f'{mark_path}/cavebot_down_mark.png'
fight_mark_path = f'{mark_path}/cavebot_fight_mark.png'

images = {
    'zoom_minus_icon': im.load_RGB2Gray(icon_zoom_minus_path),
    'zoom_plus_icon': im.load_RGB2Gray(icon_zoom_plus_path),
    'finish_mark': im.load_RGB2Gray(finish_mark_path),
    'down_mark': im.load_RGB2Gray(down_mark_path),
    'up_mark': im.load_RGB2Gray(up_mark_path),
    'fight_mark': im.load_RGB2Gray(fight_mark_path),
}

minimap_size_wh = (100, 100)
hero_pos = 50, 50
middle_mark_pos = (5, 4)  # x,y

window_game_size = (11, 15)  # for zoom -1 Height,width

# 226 up/down yellow
available_colors_to_move = [102, 111, 120, 153, 226]
