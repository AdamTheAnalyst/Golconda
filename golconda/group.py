import logging

from cliff.command import Command


class Group(Command):
    "Group something"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('Group something')
