import getopt
import sys

from client.clockClient import ClockClient
from config.clockConfig import ClockConfig
from handlers.clock import Clock
from handlers.clockCommit import ClockCommit
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from handlers.health import Health

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


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

    clock_config = ClockConfig()
    clock_config.web_address = URL

    clock_client = ClockClient(clock_config.web_address)

    commands = []


    app.run(host="0.0.0.0", port="5002", debug=True)
