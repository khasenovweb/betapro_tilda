from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from main.custom_functions.update_images_moy_skald.get_images import get_images
from main.custom_functions.update_images_moy_skald.edit_image import edit_image
from main.custom_functions.update_images_moy_skald.delete_image import delete_image
from main.custom_functions.update_images_moy_skald.add_image import add_image
from main.custom_functions.update_images_moy_skald.get_products import get_products


@csrf_exempt
def test(request):
    """ Тест """
    TOKEN = '0b4257d88e89648d5c7634fa35b563f038d657ea'
    product_id = json.loads(bytes.decode(request.body))['events'][0]['meta']['href'].split('/')[-1]
    PRODUCT_ID = product_id
    images = get_images(TOKEN, PRODUCT_ID)
    for image in images:
        if 'edit_size_khasenovweb' not in image['title']:
            img_editable = edit_image(TOKEN, image)
            delete_image(TOKEN, PRODUCT_ID, image)
            add_image(TOKEN, PRODUCT_ID, img_editable)
    return HttpResponse('Тест')