import requests



def get_images(TOKEN, PRODUCT_ID):
    """ Получаем изображения конкретного товара """
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }
    r = requests.get(f'https://online.moysklad.ru/api/remap/1.2/entity/product/{PRODUCT_ID}/images', headers=headers)

    images = r.json()['rows']
    return images
