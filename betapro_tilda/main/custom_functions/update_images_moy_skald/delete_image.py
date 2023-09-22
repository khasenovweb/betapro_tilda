import requests

def delete_image(TOKEN, PRODUCT_ID, IMAGE):
    """ Удаляем старое фото """
    IMAGE_ID = IMAGE['meta']['downloadHref'].split('/')[-1]
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }
    r = requests.delete(f'https://online.moysklad.ru/api/remap/1.2/entity/product/{PRODUCT_ID}/images/{IMAGE_ID}', headers=headers)
    print('Старое фото удалено')