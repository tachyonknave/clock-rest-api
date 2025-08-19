from src.models.clockCommand import ClockCommand


def test_clockCommand():
    expected_dict = {
        "RGB": "0x080000",
        "func": "DATE_CLOCK",
        "param": 1,
        "showTime": 10,
    }
    new_clock_command = ClockCommand()
    new_clock_command.build_command_bytes("DATE_CLOCK", 1, 10, 8, 0, 0)
    actual_dict = new_clock_command.to_dict()

    assert actual_dict == expected_dict
