from unicodedata import name
from django.urls import path, include
from . import views

# Views разнесенные по разным файлам
from main.custom_views.betapro_get_delivery_tarifs import betapro_get_delivery_tarifs


urlpatterns = [
    path('betapro_get_delivery_tarifs/', betapro_get_delivery_tarifs, name="betapro_get_delivery_tarifs"),
]