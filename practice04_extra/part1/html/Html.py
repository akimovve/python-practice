import contextlib


class Html:
    def __init__(self):
        self.data = ''

    @contextlib.contextmanager
    def body(self):
        elem = '<body>\n'
        self.data += elem

        try:
            yield {}
        except RuntimeError as err:
            print('error: ', err)
        finally:
            self.data += elem

    @contextlib.contextmanager
    def div(self):
        elem = '<div>\n'
        self.data += elem

        try:
            yield {}
        except RuntimeError as err:
            print('error: ', err)
        finally:
            self.data += elem

    def p(self, content):
        self.data += '<p>' + content + '</p>\n'
