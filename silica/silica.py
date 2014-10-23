from clint import arguments

class Silica(object):

    _handlers = {}

    def __init__(self):
        self.args = arguments.Args()

    def run(self):
        command = self._get_command()

        if command is None:
            print("No command specified, dummy")
            return

        if command not in self._handlers:
            print("No handler set for command '%s'" % command)
            return

        handler = self._handlers[command](self)
        handler.execute()

    def attach(self, command, handler):
        self._handlers[command] = handler

    def _get_command(self):
        return self.args[0]
