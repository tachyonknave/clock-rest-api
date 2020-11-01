import getopt
import json
import sys

from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse

from clockClient import send_commands
from clockCommand import ClockCommand
from health import Health

app = Flask(__name__)
api = Api(app)
CORS(app)

commands = []

clock_post_args = reqparse.RequestParser()
clock_post_args.add_argument('func', type=str, help="Function Number", required=True)
clock_post_args.add_argument('param', type=int, help="Function Parameter", )
clock_post_args.add_argument('showTime', type=int, help="Time to show function", required=True)
clock_post_args.add_argument('RGB', type=str, help="Color", required=True)


class Clock(Resource):

    def post(self):
        args = clock_post_args.parse_args()

        command = ClockCommand()

        rgb_value = args['RGB'][2:]
        red_value, green_value, blue_value = tuple(int(rgb_value[i:i + 2], 16) for i in (0, 2, 4))

        command.build_command_bytes(args['func'],
                                    args['param'],
                                    args['showTime'],
                                    red_value,
                                    green_value,
                                    blue_value)

        commands.append(command)
        return command.to_dict(), 201

    def get(self):
        json_list = []
        for cmd in commands:
            json_list.append(cmd.to_dict())
        return json_list, 200

    def delete(self):
        commands.clear()
        return 202


class ClockCommit(Resource):

    def post(self, commit):
        body_bytes = []

        for c in commands:
            body_bytes.extend(c.command_bytes)

        x = json.dumps({"commands_sent": len(commands)})
        return x, send_commands(URL, bytes(body_bytes))


api.add_resource(Clock, "/clock")
api.add_resource(ClockCommit, "/clock/<string:commit>")
api.add_resource(Health, "/health")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Need URL parameter")
        exit(1)

    URL = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:", ["help", "address="])
    except getopt.GetoptError:
        print("clockAPI.py -a http://<URL>")
        sys.exit(2)

    for o, a in opts:
        if o == "-h":
            print("clockAPI.py -a http://<URL>")
            sys.exit()
        elif o in ("-a", "--address"):
            URL = a

    app.run(host='0.0.0.0', port='5000', debug=False)
