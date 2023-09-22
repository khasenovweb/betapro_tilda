#!/bin/bash
source /var/www/betaprotilda.khasenov.ru/env/bin/activate
cd /var/www/betaprotilda.khasenov.ru/betapro_tilda/main/custom_functions/update_images_moy_skald
python3 main.py
deactivate