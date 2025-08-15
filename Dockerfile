FROM python:3.11

RUN mkdir /opt/clockRestApi
WORKDIR /opt/clockRestApi

COPY requirements.txt  /opt/clockRestApi
COPY clockAPI.py       /opt/clockRestApi
COPY clockCommand.py   /opt/clockRestApi
COPY clockClient.py    /opt/clockRestApi
COPY health.py         /opt/clockRestApi
COPY startDockerAPI.sh /opt/clockRestApi

RUN pip install -r /opt/clockRestApi/requirements.txt


EXPOSE 5000

ENTRYPOINT ["/opt/clockRestApi/startDockerAPI.sh"]