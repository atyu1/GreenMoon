
class HandlerError(Exception):
    """ Common Errors with Handler """
    pass


class Handler(HandlerError):
    """ Common class for all Handlers """

    def save(self):
        return
