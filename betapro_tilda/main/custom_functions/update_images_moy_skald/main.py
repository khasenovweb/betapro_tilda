from get_images import get_images
from edit_image import edit_image
from delete_image import delete_image
from add_image import add_image
from get_products import get_products


TOKEN = '0b4257d88e89648d5c7634fa35b563f038d657ea'


i = True
while i == True:
    products = get_products(TOKEN)

    for el in products:
        PRODUCT_ID = el['id']
        images = get_images(TOKEN, PRODUCT_ID)
        for image in images:
            if 'edit_size_khasenovweb' not in image['title']:
                img_editable = edit_image(TOKEN, image)
                delete_image(TOKEN, PRODUCT_ID, image)
                add_image(TOKEN, PRODUCT_ID, img_editable)

