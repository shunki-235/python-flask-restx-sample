from flask import Flask, jsonify
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# app.config["SQLALCHEMY_DATABASE_URI"]

db = SQLAlchemy(app)


@api.route('/users')
class Users(Resource):
    def get(self):
        return jsonify({"message": "Hello World"})

    def post(self):
        pass


@api.route('/user<int:id>')
class UserResource(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


if __name__ == "__main__":
    app.run(debug=True)
