from unicodedata import name
from django.urls import path, include
from . import views

# Views разнесенные по разным файлам
from main.custom_views.betapro_get_delivery_tarifs import betapro_get_delivery_tarifs
from main.custom_views.test import test
from main.custom_views.update_image_moy_skald import update_image_moy_skald


urlpatterns = [
    path('betapro_get_delivery_tarifs/', betapro_get_delivery_tarifs, name="betapro_get_delivery_tarifs"),
    path('test/', test, name="test"),
    path('update_image_moy_skald/', test, name="update_image_moy_skald"),
]