import os
import jinja2


class Controller(object):
    def __init__(self, server):
        self.__server = server

    @property
    def server(self):
        return self.__server

    @staticmethod
    def render(filename, context):
        template = jinja2.Environment(
            loader=jinja2.FileSystemLoader('views/')
        ).get_template(filename).render(context)

        return bytes(template, 'utf-8')
