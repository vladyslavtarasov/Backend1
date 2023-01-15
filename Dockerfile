FROM python:3.11.0

ENV FLASK_APP=backend_labs
ENV JWT_SECRET_KEY=29419470832039429030642183190337617065

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY backend_labs /opt/backend_labs

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT