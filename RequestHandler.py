from http.server import BaseHTTPRequestHandler
from route import Router
from controllers import HomeController, ContentController, APIController


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        routes = [
            {'regexp': r'^/$', 'controller': HomeController, 'action': 'indexAction'},
            {'regexp': r'^/content/', 'controller': ContentController, 'action': 'showAction'},
            {'regexp': r'^/api/', 'controller': APIController, 'action': 'indexAction'}
        ]

        self.__router = Router(self)
        for route in routes:
            self.__router.addRoute(route['regexp'], route['controller'], route['action'])

        BaseHTTPRequestHandler.__init__(self, request, client_address, server)

    def do_GET(self):
        self.__router.route(self.path)
