#!/usr/bin/python3

from sensor.dht11 import Dht11Sensor as Sensor
from dotenv import load_dotenv
import os
import logger

def main():

    load_dotenv()

    dht = Sensor()
    data = dht.run()

    print (data)

def __name__=="__main__":
    main()