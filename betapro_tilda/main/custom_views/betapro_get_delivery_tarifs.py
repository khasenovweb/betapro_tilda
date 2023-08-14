from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

from main.custom_functions.plural_days import plural_days


def betapro_get_delivery_tarifs(request):
    """ Получаем тарифы на доставку через API фулфилмента Betapro """

    # addr = "г Челябинск ул Александра Шмакова 17А"
    addr = request.GET.get('addr')
    weight = request.GET.get('weight') #0.221

    xml = f"""
    <request request_type="54" partner_id="201" password="test">
        <parcel 
            sum_vl="2139" 
            volume="0.0006684" 
            weight="{weight}" 
            sum_nalog="2139" 
            addr="{addr}" 
            zip="664020" 
            version="1"
        />
    </request>
    """.encode()

    headers = {
        'Content-Type': 'text/xml',
        'X-Requested-With': 'XMLHttpRequest',
    }

    r = requests.post('http://api.betapro.ru:8080/bp/hs/wsrv',  data=xml, headers=headers, verify=False)

    soup = BeautifulSoup(r.text, features="html.parser")

    sd_all = soup.find_all('sd')
    sd_all_json = []
    for el in sd_all:
        sd_name = el.get('sd_name')
        tariff_name = el.get('tariff_name')
        tariff = el.get('tariff')
        tariff_round = round(float(el.get('tariff')))
        days = el.get('days')
        days_text = plural_days(int(days.split('-')[-1]))
        sd_all_json.append({
            'sd_name': sd_name,
            'tariff_name': tariff_name,
            'tariff': tariff,
            'tariff_round': tariff_round,
            'days': days,
            'days_text': f'{days} {days_text}',
        })
        # print('------------------------')
        # print(f"{tariff_name} {tariff} руб. {days} дней")
        # print('------------------------')
    context = {
        'tarifs': sd_all_json
    }
    return JsonResponse(context)




