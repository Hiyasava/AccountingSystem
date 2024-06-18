FROM python:3.11-slim

WORKDIR /app
COPY . /app/

RUN apt-get update \
&& apt-get -y install libpq-dev gcc \
&& pip install -r requirements.txt

CMD python manage.py makemigrations \
    && python manage.py migrate \ 
    && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell \
    && python manage.py runserver 0.0.0.0:8000