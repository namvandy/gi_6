FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/namvandy/gi_6.git

WORKDIR /home/gi_6/

RUN echo "SECRET_KEY=django-insecure-(0gz$r4fdh82)wppex72sz-^!$xvyna@u_&owxeahtx^^n8z91" > .env

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]