#!/bin/bash
source /var/www/betaprotilda.khasenov.ru/env/bin/activate
cd /var/www/betaprotilda.khasenov.ru/betapro_tilda
daphne -p 8001 betapro_tilda.asgi:application
deactivate