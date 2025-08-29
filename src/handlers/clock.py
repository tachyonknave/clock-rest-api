from flask_restful import Resource, reqparse
from http import HTTPStatus

from icecream import ic

import services

class Clock(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "func", type=str, required=True
        )
        self.parser.add_argument(
            "param", type=int, required=False, default=0
        )
        self.parser.add_argument(
            "showTime", type=int, required=True
        )
        self.parser.add_argument(
            "RGB", type=str, required=True
        )
        super(Clock,self).__init__()
    def post(self):

        args = self.parser.parse_args()

        ic(args['showTime'])
        command_dict = services.clock_service.add_command(
            args['func'],
            args['param'],
            args['showTime'],
            args['RGB'])

        return command_dict, HTTPStatus.CREATED

    def get(self):
        json_list = []
        for cmd in services.clock_service.get_commands():
            json_list.append(cmd.to_dict())
        return json_list, HTTPStatus.OK

    def delete(self):
        services.clock_service.clear_commands()
        return HTTPStatus.ACCEPTED
