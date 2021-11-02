
from .sensor import Sensor, SensorError

import time
import adafruit_dht

_PIN = 4


class Dht11Sensor(Sensor):
    """ DHT11 Sensor """

    def __init__(self):
        super().__init__(self)
        self.sensor = adafruit_dht.DHT11(_PIN)

    def run(self):
        try:
            temperature = {"temperature": self.sensor.temperature}
            humidity = {"humidity": self.sensor.humidity}
            return {"data": [temperature, humidity]}
        except RuntimeError as error:
            raise SensorError(f"Wrong data from DHT11 sensor, {error.args[0]}")
