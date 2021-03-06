#!/usr/bin/python3

from sensor.dht11 import Dht11Sensor as Sensor
from handler.greenPlanetApi import GreenPlanetApi as GPA
import os
import logging

from sensor.sensor import SensorError
from src.handler.handler import HandlerError


def main():

    mysense = Sensor()
    data = {}

    try:
        data = mysense.run()
    except SensorError as e:
        logging.error(f"Issue with Sensor: {e}")
    except HandlerError as e:
        logging.error(f"Issue with Handler: {e}")

    gpa = GPA(raw_data=data)
    gpa.save()


if __name__ == "__main__":
    main()
