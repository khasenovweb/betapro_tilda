import requests
import json
import random


def add_image(TOKEN, PRODUCT_ID, IMAGE):
    """ Добавляем фото к товару """
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        "Content-Type": "application/json"
    }
    data = {
        "filename": f"edit_size_khasenovweb_{random.randint(1111111111, 9999999999)}.png",
        "content": IMAGE
    }
    r = requests.post(f'https://online.moysklad.ru/api/remap/1.2/entity/product/{PRODUCT_ID}/images', headers=headers, json=data)
    print(f"Новое фото добавлено: {r}")