from client.clockClient import ClockClient
from models.clockCommand import ClockCommand

from icecream import ic

class ClockService:

    def __init__(self, URL):
        self.clock_client = ClockClient(URL)
        self.commands = []

    def add_command(self, function, param, show_time, rgb):
        command = ClockCommand()

        if rgb[0:2] == "0x":
            rgb_value = rgb[2:]
        elif rgb[0] == "#":
            rgb_value = rgb[1:]
        else:
            rgb_value = rgb

        red_value, green_value, blue_value = tuple(
            int(rgb_value[i: i + 2], 16) for i in (0, 2, 4)
        )

        ic(show_time, red_value, green_value, blue_value)

        command.build_command_bytes(
            function,
            param,
            show_time // 100, # convert ms to deci-seconds
            red_value // 32,
            green_value // 32,
            blue_value // 32,
        )

        self.commands.append(command)

        return command.to_dict()

    def clear_commands(self):
        self.commands = []

    def get_commands(self):
        return self.commands

    def send_commands(self):
        return self.clock_client.send_commands(self.commands)
