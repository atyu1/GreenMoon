import requests
from .handler import Handler, HandlerError
from cerberus import Validator
from time import time
from os import environ as env
import logging

_TIMEOUT = 20
_DATA_SCHEMA = {
    "timestamp": {"type": "float"},
    "location": {"type": "string"},
    "room": {"type": "string"},
    "name": {"type": "string"},
    "datapoints": {
        "type": "dict",
        "schema": {
            "sensor": {"type": "string"},
            "value": {"type": "float"}
        }
    }
}


class GreenPlanetApi(Handler):
    """ Api to communicate with external API server"""
    """ TODO: Add auth and TLS """

    def __init__(self, raw_data=[]):
        super().__init__(self)
        self._raw_data = raw_data
        self._load_config()

        self.data = self.prepare_data()

    def _timestamp(self):
        """ Set timestamp variable"""
        self.timestamp = time()
        logging.debug(f"Timestamp loaded: {self.timestamp}")

    def _load_location(self):
        """ Load 'location' Config from OS Environemnt variable """
        try:
            self.location = env['GREENMOON_LOCATION']
        except KeyError:
            raise HandlerError(
                f"Missing 'GREENMOON_LOCATION' environment variable")

        logging.debug(f"Location loaded from env: {self.location}")

    def _load_room(self):
        """ Load 'room' Config from OS Environemnt variable """
        try:
            self.room = env['GREENMOON_ROOM']
        except KeyError:
            raise HandlerError(
                f"Missing 'GREENMOON_ROOM' environment variable")

        logging.debug(f"Room loaded from env: {self.room}")

    def _load_name(self):
        """ Load 'name' Config from OS Environemnt variable """
        try:
            self.name = env['GREENMOON_NAME']
        except KeyError:
            raise HandlerError(
                f"Missing 'GREENMOON_NAME' environment variable")

        logging.debug(f"Room loaded from env: {self.room}")

    def _load_url(self):
        """ Load 'url' Config from OS Environemnt variable """
        try:
            self.url = env['GREENPLANET_URL']
        except KeyError:
            raise HandlerError(
                f"Missing 'GREENPLANET_URL' environment variable")

        logging.debug(f"Room loaded from env: {self.room}")

    def _load_config(self):
        """ Load all required config from OS Environemnt variables """
        self._timestamp()
        self._load_location()
        self._load_room()
        self._load_url()

    def validate(self, tmp_data):
        """ Be sure that data have proper format """
        v = Validator(_DATA_SCHEMA)

        if v.validate(tmp_data):
            logging.info("Data passed the Validation")
            logging.debug(f"Data after validation: {tmp_data}")
        else:
            raise HandlerError(
                f"Validation issue with data from sensors: {v.errors}")

    def prepare_data(self):
        """ We need to put together the sensor data and metadata"""
        tmp_data = {
            "timestamp": self.timestamp,
            "location": self.location,
            "room": self.room,
            "datapoints": self.raw_data["data"]
        }

        return tmp_data

    def save(self):
        """ Sending the data via API """
        self.validate()

        try:
            r = requests.post(self.url, data=self.data, timeout=_TIMEOUT)
            r.raise_for_status()
        except requests.exceptions.Timeout:
            raise HandlerError(
                f"GREENPLANET HTTP timeout after {_TIMEOUT} seconds!")
        except requests.exceptions.ConnectionError:
            raise HandlerError(
                f"GREENPLANET HTTP connectivity issue, check reachability and DNS for {self.url}")
        except requests.exceptions.HTTPError as e:
            raise HandlerError(
                f"GREENPLANET HTTP returned a non successful code: {r.status_code}: {e.args[0]}")
