import requests


def send_commands(web_address, command_bytes):
    headers = {'Content-Type': 'application/octet-stream'}
    response = requests.post(web_address, data=command_bytes, headers=headers)

    return response.status_code
