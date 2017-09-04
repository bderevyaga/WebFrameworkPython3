from controllers.Controller import Controller


class HomeController(Controller):
    def __init__(self, server):
        Controller.__init__(self, server)

    def indexAction(self):
        self.server.send_response(200)
        self.server.send_header('Content-type', 'text/html')
        self.server.end_headers()
        self.server.wfile.write(b'Home!!!!')
