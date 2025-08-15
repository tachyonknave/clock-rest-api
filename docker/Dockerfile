FROM python:3.11

WORKDIR /opt/clockRestApi

# Copy requirements first to leverage layer caching
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application source code
COPY ./src/clockAPI.py .
COPY ./src/clockCommand.py .
COPY ./src/clockClient.py .
COPY ./src/health.py .

# Copy the startup script and make it executable
COPY docker/startDockerAPI.sh .
RUN chmod +x startDockerAPI.sh


EXPOSE 5000

ENTRYPOINT ["./startDockerAPI.sh"]