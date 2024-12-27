from flask_restx import Namespace, Resource

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"hello":"restx"}