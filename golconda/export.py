import logging

from cliff.command import Command


class Export(Command):
    "Export something"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('Export something')
