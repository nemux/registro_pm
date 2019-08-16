from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def post(self):
        #printing request.data works
        json_data = request.get_json(force=True) # this issues Bad request
        # request.json also does not work
        return json_data['hello'], 201

api.add_resource(Test, '/')

if __name__ == '__main__':
    app.run(debug=True)
