import requests



def get_products(TOKEN):
    """ Получаем все товары """
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }
    r = requests.get(f'https://online.moysklad.ru/api/remap/1.2/entity/product', headers=headers)

    products = r.json()['rows']

    return products
