import requests
from icecream import ic

class ClockClient:

    def __init__(self, web_address):
        self.web_address = web_address

    def send_commands(self, clock_commands):

        body_bytes = bytearray()

        for c in clock_commands:
            body_bytes.extend(c.command_bytes)

        headers = {"Content-Type": "application/octet-stream"}

        ic(body_bytes)

        status_code = 500
        try:
            response = requests.post(self.web_address, data=body_bytes, headers=headers)
            status_code = response.status_code
        except TypeError:
            print("TypeError")

        return status_code
