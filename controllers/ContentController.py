from controllers.Controller import Controller
import os


class ContentController(Controller):
    CONTENT_BASE_PATH = 'public/'
    CONTENT_TYPE = {
        '.ico': 'image/x-icon',
        '.html': 'text/html',
        '.js': 'text/javascript',
        '.json': 'application/json',
        '.css': 'text/css',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.wav': 'audio/wav',
        '.mp3': 'audio/mpeg',
        '.svg': 'image/svg+xml',
        '.pdf': 'application/pdf',
        '.doc': 'application/msword'
    }

    def __init__(self, server):
        Controller.__init__(self, server)

    def showAction(self):
        filename = self.CONTENT_BASE_PATH + self.server.path[9:]

        if os.access(filename, os.R_OK) and not os.path.isdir(filename):
            file = open(filename, "rb")
            content = file.read()
            file.close()

            extension = os.path.splitext(filename)[1]

            self.server.send_response(200)
            self.server.send_header('Content-type', self.CONTENT_TYPE[extension])
            self.server.end_headers()
            self.server.wfile.write(content)
        else:
            self.server.send_response(404)
            self.server.end_headers()
