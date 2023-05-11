#!/bin/sh

if [ "$DATABASE" = "postgres_db" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic

echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', '','admin' )" | python manage.py shell


exec "$@"
