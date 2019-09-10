import logging
import json
from cliff.command import Command
from datetime import datetime
from uuid import uuid4


class Create(Command):
    "Create a new diamond"

    log = logging.getLogger(__name__)

    def text_input(self, label, schema):

        if "description" in schema:
            print("\n")
            self.log.info(schema["description"])

        if schema["type"] in ["string", "integer"]:
            # Parse Valid Options
            if "enum" in schema:
                options = "[{}]".format("|".join(schema["enum"]))
            else:
                options = ""

            if "format" in schema:
                if schema["format"] == "uuid":
                    schema["default"] = str(uuid4())

            if "default" in schema:
                default = "[Default: {}]".format(schema["default"])
            else:
                default = ""

            value = input("{} {}{}: ".format(
                label,
                options,
                default,
            ))

            # No Value Supplied
            if value == "" and "default" in schema:
                value = schema["default"]
            elif value == "":
                self.log.info('Please set a value')
                value = self.text_input(label, schema)

            # If Illegal Option
            if "enum" in schema:
                if value not in schema["enum"]:
                    self.log.info('Please choose a valid option')
                    value = self.text_input(label, schema)

        elif schema["type"] == "date-time":

            # Handle Date Time Default Now
            value = input("{} [Default: {}]: ".format(
                label,
                datetime.now().isoformat()
            ))

            # No Value Supplied
            if value == "" and "default" in schema:
                value = datetime.now().isoformat()
            elif value == "":
                self.log.info('Please set a value')
                value = self.text_input(label, schema)

        elif schema["type"] == "array":

            values = []
            value = ""
            self.log.info('Enter "." (no quotes) for any value to finish.')
            while value != ".":
                resource = {}
                for field in schema["items"]["properties"]:
                    value = self.text_input(
                        '(array item)> {}'.format(field),
                        schema["items"]["properties"][field])
                    if value == ".":
                        break
                    else:
                        resource[field] = value
                if value != ".":
                    values.append(resource)
            value = values
        return value

    def parser(self, schema, state, headings=None):
        if not headings:
            headings = []

        for key in schema:
            subheadings = headings.copy()
            subheadings.append(key)
            if schema[key]["type"] == "object":
                state[key] = {}
                state[key] = self.parser(
                    schema[key]["properties"],
                    state[key],
                    headings=subheadings)
            else:
                state[key] = self.text_input(
                    '{}'.format(' > '.join(subheadings)),
                    schema[key])

        return(state)

    def take_action(self, args):
        self.log.info('Create a new diamond')
        with open('golconda/schema/schema.json', 'r') as f:
            schema = json.loads(f.read())
            record = self.parser(schema, {})
            self.app.db.golcunda.insert_one(record)
            print("Diamond {} stored".format(record["_id"]))
