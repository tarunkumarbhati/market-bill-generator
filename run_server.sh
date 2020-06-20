#!/bin/bash
set -e

python manage.py migrate
python add_item_prices.py
python add_discount_rules.py
python manage.py runserver 0.0.0.0:8000