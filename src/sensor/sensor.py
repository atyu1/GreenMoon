class SesnsorError(Exception):
    """ Common Error Class for all Sensors """
    pass

class Sensor(SesnsorError):
    """ Base class for all Sensors """

    def run(self):
        raise NotImplementedError("Please create a child sensor for more direct usage")