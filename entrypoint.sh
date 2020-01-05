#! /bin/sh

sleep 30

python3 manage.py migrate
python3 manage.py loaddata dump.json
python3 manage.py collectstatic --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('aherman59', 'antoine.herman@cerema.fr', 'Cerem@59')" | python3 manage.py shell

/usr/bin/gunicorn appff.wsgi:application -w 2 -b :8000

