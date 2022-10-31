FROM python:3.11.0

ENV FLASK_APP=lab1

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY lab1 /opt/lab1

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT