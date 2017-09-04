class Controller(object):
    def __init__(self, server):
        self.__server = server

    @property
    def server(self):
        return self.__server
