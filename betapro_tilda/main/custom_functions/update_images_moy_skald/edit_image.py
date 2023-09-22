import requests

from PIL import Image
from io import BytesIO
import base64


def edit_image(TOKEN, IMAGE):
    """ Редактируем конкретное изображение """
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }
    r = requests.get(IMAGE['meta']['downloadHref'], headers=headers)

    image_base_64 = base64.b64encode(r.content)
    im = Image.open(BytesIO(base64.b64decode(image_base_64)))

    thumbnail_size = (1700, 1700)
    im.thumbnail( thumbnail_size )

    width = im.size[0]
    height = im.size[1]

    if width > height:
        if width < 1700:
            resize_width_percent = ((1700 - width) * 100) / width
            resize_height = round( (height * resize_width_percent) / 100 )
            resize_height = height + resize_height
            im = im.resize( (1700,resize_height) )
    else:
        if height < 1700:
            resize_height_percent = ((1700 - height) * 100) / height
            resize_width = round( (width * resize_height_percent) / 100 )
            resize_height = width + resize_width
            im = im.resize( (resize_width, 1700) )
    
    width = im.size[0]
    height = im.size[1]

    width_new = 1920
    height_new = 1920

    left_new = round( (width_new - width) / 2 )
    # top_new = round( (height_new - height) / 2 )
    top_new = (height_new - 500) - height

    im2 = Image.new(color=('#ffffff'), size=(width_new,height_new), mode="RGB")
    im2.paste(im, (left_new,top_new))

    im2_byte = BytesIO()
    im2.save(im2_byte, format='PNG')
    im2_base64 = base64.b64encode(im2_byte.getvalue())
    im2_base64 = bytes.decode(im2_base64, 'utf-8')

    return im2_base64
    # im2.save(f"edit_{I}.png")