FROM python:3.9.0

WORKDIR /home/

RUN echo "dkanshfo"

RUN git clone https://github.com/namvandy/gi_6.git

WORKDIR /home/gi_6/

#RUN echo "SECRET_KEY=django-insecure-(0gz$r4fdh82)wppex72sz-^!$xvyna@u_&owxeahtx^^n8z91" > .env

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c","python manage.py collectstatic --noinput --settings=gis_2.settings.deploy && python manage.py migrate --settings=gis_2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=gis_2.settings.deploy gis_2.wsgi --bind 0.0.0.0:8000"]