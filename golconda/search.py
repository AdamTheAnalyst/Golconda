import logging
import json
from cliff.lister import Lister


class Search(Lister):
    """Search for something"""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Search, self).get_parser(prog_name)
        parser.add_argument(
            'query',
            type=str,
            help='query help')
        parser.add_argument('--filter',
                            type=str,
                            required=False,
                            help='filter string',
                            default='{ "_author": 1, "_thread": 1 }')

        return parser

    def take_action(self, parsed_args):
        if hasattr(parsed_args, "query"):
            query = json.loads(parsed_args.query)
            filter = json.loads(parsed_args.filter)
            result = self.app.db.golcunda.find(query, filter)
            columns = ["_id"]
            for k in filter:
                columns.append(k)
            data = []
            for item in result:
                row = []
                for k in item:
                    row.append(item[k])
                data.append(row)
            return columns, data
