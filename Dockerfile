FROM python:3.10

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x /wait-for-it.sh

CMD python3 manage.py runserver 0.0.0.0:8000
