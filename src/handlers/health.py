from flask_restful import Resource
from http import HTTPStatus


class Health(Resource):
    def get(self):
        return "OK", HTTPStatus.OK
