#!/bin/sh

pip install -r requirements.txt
python manage.py makemigrations users
python manage.py migrate
python manage.py loaddata seeds/user.json
python manage.py loaddata seeds/book.json
python manage.py loaddata seeds/favouritebooks.json
python manage.py runserver 0.0.0.0:8000