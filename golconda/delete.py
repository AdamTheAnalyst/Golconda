import logging
from bson import json_util
import json
from cliff.command import Command


class Delete(Command):
    "Delete something"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Delete, self).get_parser(prog_name)
        subparser1 = parser.add_subparsers(help='Diamond ID To Delete')

        # add a subcommand
        parser_a = subparser1.add_parser(
            'diamond',
            help='diamond help'
        )
        parser_a.add_argument(
            'diamond_id',
            type=str,
            help='Diamond ID to delete'
        )

        return parser

    def take_action(self, parsed_args):

        if hasattr(parsed_args, "diamond_id"):
            # Delete Diamond Document
            result = self.app.db.golcunda.delete_one(
                {"_id": parsed_args.diamond_id}
            )
            self.log.info(
                json.dumps(
                    result,
                    default=json_util.default,
                    indent=4
                ))
