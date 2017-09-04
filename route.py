import re


class Router(object):
    def __init__(self, server):
        self.__routes = []
        self.__server = server

    def addRoute(self, regexp, controller, action):
        self.__routes.append({'regexp': regexp, 'controller': controller, 'action': action})

    def route(self, path):
        for route in self.__routes:
            if re.search(route['regexp'], path):
                cls = route['controller']
                func = cls.__dict__[route['action']]
                obj = cls(self.__server)
                func(obj)
                return

        self.__server.send_response(404)
        self.__server.end_headers()
