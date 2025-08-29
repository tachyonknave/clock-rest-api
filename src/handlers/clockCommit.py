from flask_restful import Resource

import services

class ClockCommit(Resource):
    def post(self):
        return services.clock_service.send_commands()
