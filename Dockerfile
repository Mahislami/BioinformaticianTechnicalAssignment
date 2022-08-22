#FROM python:3.10
#
#WORKDIR /core
#
#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
#
#COPY . .
#
#RUN chmod +x /core/wait-for-it.sh
#
#CMD python3 manage.py runserver 0.0.0.0:8000

FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 manage.py runserver 0.0.0.0:8000