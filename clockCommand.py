from enum import Enum


class FuncEnum(Enum):
    TWELVE_CLOCK = 0
    TWENTY_FOUR_CLOCK = 1
    DATE_CLOCK = 2
    MINUTE_COUNTDOWN = 3
    DAY_COUNTDOWN = 4
    MINUTE_TIMER = 5
    SECOND_TIMER = 6
    TIMEZONE = 7


class ClockCommand:
    def __init__(self):
        self.function = ""
        self.parameter = 0
        self.show_time = 0
        self.red = 0
        self.green = 0
        self.blue = 0
        self.command_bytes = []

    def build_command_bytes(self, function_name, parameter, show_time, red, green, blue):
        # From server code:
        #  FunctionCodeIndex = 0;
        #  DutyCycleIndex = 1;
        #  ParameterHigh = 2;
        #  ParameterLow = 3;
        #  RGB_Red = 4;
        #  RGB_Green = 5;
        #  RGB_Blue = 6;

        self.function = function_name
        self.parameter = parameter
        self.show_time = show_time
        self.red = red
        self.green = green
        self.blue = blue

        if parameter is None:
            parameter = "0"

        function = FuncEnum[function_name]

        command_ints = [function.value,
                        int(show_time),
                        int(parameter) >> 8, int(parameter) & 0xFF,
                        int(red), int(green), int(blue)]

        self.command_bytes = bytes(command_ints)

    def to_dict(self):
        rgb_string = "0x{:02x}{:02x}{:02x}"

        return {'func': self.function, 'param': self.parameter, 'showTime': self.show_time,
                'RGB': rgb_string.format(self.red, self.green, self.blue)}
