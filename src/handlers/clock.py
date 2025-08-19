from models.clockCommand import ClockCommand
from flask_restful import Resource


class Clock(Resource):
    def __init__(self):
        self.commands = []

    def post(self, args):

        command = ClockCommand()

        if args["RGB"][0:2] == "0x":
            rgb_value = args["RGB"][2:]
        elif args["RGB"][0] == "#":
            rgb_value = args["RGB"][1:]
        else:
            rgb_value = args["RGB"]

        red_value, green_value, blue_value = tuple(
            int(rgb_value[i : i + 2], 16) for i in (0, 2, 4)
        )

        command.build_command_bytes(
            args["func"],
            args["param"],
            args["showTime"],
            red_value // 32,
            green_value // 32,
            blue_value // 32,
        )

        self.commands.append(command)
        return command.to_dict(), 201

    def get(self):
        json_list = []
        for cmd in self.commands:
            json_list.append(cmd.to_dict())
        return json_list, 200

    def delete(self):
        self.commands.clear()
        return 202
