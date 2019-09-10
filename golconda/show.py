import logging
from bson import json_util
import json
from cliff.show import ShowOne


class Show(ShowOne):
    "Show for something"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Show, self).get_parser(prog_name)
        subparser1 = parser.add_subparsers(help='sub-command help')

        # add a subcommand
        parser_a = subparser1.add_parser('diamond', help='diamond help')
        parser_a.add_argument('diamond_id', type=str, help='diamond_id help')

        return parser

    def take_action(self, parsed_args):

        if hasattr(parsed_args, "diamond_id"):
            # Get Diamond Document
            result = self.app.db.golcunda.find_one(
                {"_id": parsed_args.diamond_id}
            )

            columns = []
            data = []
            for k in result:
                columns.append(k)
                data.append(json.dumps(
                    result[k],
                    default=json_util.default,
                    indent=4
                ))
            return (columns, data)
