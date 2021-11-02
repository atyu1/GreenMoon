from .handler import Handler, HandlerError
from time import time
from os import environ as env

class GreenPlanetApi(Handler):
    """ Api to communicate with external API server"""
    def __init__(self, data=[]):
        super().__init__(self)
        self._data = data
        self._load_config()

    def _timestamp(self):
        """ Set timestamp variable"""
        self.timestamp = time()

    def _load_location(self):
        """ Load 'location' Config from OS Environemnt variable """
        try:
            self.location=env['GREENMOON_LOCATION']
        except KeyError:
            raise HandlerError(f"Missing 'GREENMOON_LOCATION' environment variable")
    
    def _load_room(self):
        """ Load 'room' Config from OS Environemnt variable """
        try:
            self.location=env['GREENMOON_ROOM']
        except KeyError:
            raise HandlerError(f"Missing 'GREENMOON_LOCATION' environment variable")
    
    def _load_config(self):
        """ Load all required config from OS Environemnt variables """
        self._timestamp()
        self._load_location()
        self._load_room()
    
    def validate(self):
        pass

    def prepare_data(self):
        pass

    def save(self):
        pass
    