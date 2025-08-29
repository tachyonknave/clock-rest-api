import getopt
import sys

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from handlers.clock import Clock
from handlers.clockCommit import ClockCommit
from handlers.health import Health

import services
from service.clockService import ClockService


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Need URL parameter")
        exit(1)

    URL = ""
    server_port = 5001

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ha:", ["help", "address="])
    except getopt.GetoptError:
        print("clockAPI.py -a http://<URL>")
        sys.exit(2)

    for opt, argument in opts:
        if opt == "-h":
            print("clockAPI.py -a http://<URL>")
            sys.exit()
        elif opt in ("-a", "--address"):
            URL = argument
        elif opt in ("-p", "--port"):
            server_port = int(argument)

    services.clock_service = ClockService(URL)

    app = Flask(__name__)
    api = Api(app)
    cors = CORS(app)

    api.add_resource(Clock, "/clock")
    api.add_resource(ClockCommit, "/clock/commitCommands")
    api.add_resource(Health, "/health")

    app.run(host="0.0.0.0", port=server_port, debug=True)
