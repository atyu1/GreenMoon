from sensor.sensor import Sensor
from sensor.sensor import SensorError

import time
import board
import adafruit_dht
from src import sensor

_PIN = board.D23


class Dht11Sensor(Sensor):
    """ DHT11 Sensor """
    def __init__(self):
        self.sensor = adafruit_dht.DHT11(_PIN)
    
    def run(self):
        try:
            temperature = {"temperature": sensor.temperature}
            humidity = {"humidity": sensor.humidity}
            return {"data":[temperature, humidity]}
        except RuntimeError as error:
            raise SensorError(f"Wrong data from DHT11 sensor, {error.args[0]}")
