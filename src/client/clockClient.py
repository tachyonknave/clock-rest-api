import requests


class ClockClient:

    def __init__(self, web_address):
        self.web_address = web_address

    def send_commands(self, command_bytes):
        headers = {"Content-Type": "application/octet-stream"}
        response = requests.post(self.web_address, data=command_bytes, headers=headers)

        return response.status_code
