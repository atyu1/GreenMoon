#!/usr/bin/python3

from sensor.dht11 import Dht11Sensor as Sensor
import os
import logging

from sensor.sensor import SensorError


def main():

    dht = Sensor()
    try:
        data = dht.run()
    except SensorError as e:
        logging.error(f"Issue with DHT Sensor: {e}")

    print(data)


if __name__ == "__main__":
    main()
