import pathlib
import src.utils.image as im

dir_path = pathlib.Path(__file__).parent.resolve()
images_path = f'{dir_path}/images'

icon_zoom_minus_path = f'{images_path}/zoom_minus.png'
icon_zoom_plus_path = f'{images_path}/zoom_plus.png'

images = {
    'zoom_minus_icon': im.load_RGB2Gray(icon_zoom_minus_path),
    'zoom_plus_icon': im.load_RGB2Gray(icon_zoom_plus_path)
}

minimap_size_wh = (100, 100)
