#!/usr/bin/python3

from sensor.dht11 import Dht11Sensor as Sensor
import os
import logger

def main():

    dht = Sensor()
    data = dht.run()

    print (data)

if __name__== "__main__":
    main()