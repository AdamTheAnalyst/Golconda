#!/usr/bin/python
import sys
import pymongo
from cliff.app import App
from cliff.commandmanager import CommandManager


class GolcondaApp(App):

    def __init__(self):
        super(GolcondaApp, self).__init__(
            description='Golconda CLI: The Diamond Model Explorer',
            version='0.1',
            command_manager=CommandManager('golconda.cli'),
            deferred_help=True,
            )

    def initialize_app(self, argv):
        self.LOG.debug('Initializing')
        self._client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self._client["golcunda"]

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)


def main(argv=sys.argv[1:]):
    myapp = GolcondaApp()
    return myapp.run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
