from http.server import HTTPServer
from RequestHandler import RequestHandler

PORT = 8082
SERVER = '127.0.0.1'


def main():
    httpd = HTTPServer((SERVER, PORT), RequestHandler)

    try:
        print('Server started http://%s:%s' % (SERVER, PORT))
        httpd.serve_forever()
    except ZeroDivisionError:
        print('Server shutting down')
        httpd.socket.close()


main()
