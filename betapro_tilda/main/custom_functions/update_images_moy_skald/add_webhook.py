
import requests

def add_webhook(TOKEN):
    """ Добавление вебхука """
    # headers = {
    #     'Authorization': f'Bearer {TOKEN}',
    #     "Content-Type": "application/json"
    # }
    # r = requests.get('https://online.moysklad.ru/api/remap/1.2/entity/webhook', headers=headers)
    # print(r.text)
    headers = {
        'Authorization': f'Bearer {TOKEN}',
        "Content-Type": "application/json"
    }
    data = {
        "url": "https://betaprotilda.khasenov.ru/test/",
        "action": "UPDATE",
        "entityType": "product"
    }
    r = requests.post('https://online.moysklad.ru/api/remap/1.2/entity/webhook', headers=headers, json=data)
    print(r.text)



