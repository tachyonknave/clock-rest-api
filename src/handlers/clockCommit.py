from flask_restful import  Resource

import json


class ClockCommit(Resource):
    def post(self, commands):
        body_bytes = []

        for c in commands:
            body_bytes.extend(c.command_bytes)

        x = json.dumps({"commands_sent": len(commands)})
        return x, clock_client.send_commands(bytes(body_bytes))
