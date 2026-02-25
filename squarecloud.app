DISPLAY_NAME=Gestao Raul API
DESCRIPTION=Sistema de Gestão para Restaurantes/Bares com API REST.
MAIN=gestaoRaul/wsgi.py
MEMORY=512
VERSION=recommended
SUB_DOMAIN=gestao-raul # Escolha um subdomínio disponível
START=python manage.py collectstatic --noinput && python -m gunicorn gestaoRaul.wsgi:application --bind 0.0.0.0:80 --timeout 120
