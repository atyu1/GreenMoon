FROM python:3
COPY requirements.txt .
ARG sensor_name
RUN pip3 install -r requirements.txt

COPY src/handler /var/app/src
COPY src/sensor/__init__.py /var/app/src
COPY src/sensor/sensor.py /var/app/src
COPY src/sensor/$sensor_name.py /var/app/src
COPY src/app_$sensor_name.py /var/app/src

WORKDIR /var/app/src
CMD["python3", "app_$sensor_name.py"]