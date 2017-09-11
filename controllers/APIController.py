import json

from controllers.Controller import Controller


class APIController(Controller):
    def __init__(self, server):
        Controller.__init__(self, server)

    def indexAction(self):
        self.server.send_response(200)
        self.server.send_header('Content-type', 'text/json')
        self.server.end_headers()
        self.server.wfile.write(bytes(json.dumps({'test': 123}), 'utf-8'))
