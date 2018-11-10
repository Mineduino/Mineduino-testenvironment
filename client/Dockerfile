FROM python:3.7.1-alpine
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV MQTTIP="broker"
ENV MQTTPORT=1883
ENV TOPIC=temp
#may be button/dht12
ENV TYPE="dht12"

COPY main.py ./

ENTRYPOINT ["python", "-u", "main.py"]
