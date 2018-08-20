from flask import Flask
from flask_restplus import Resource,Api
import json
from flask import jsonify
from config import app_config
from models import db,bcrypt

def create_app(env_name):
    app=Flask(__name__)
    app.config.from_object(app_config[env_name])
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' 
    bcrypt.init_app(app)
    db.init_app(app)
    api=Api(app)


    @api.route("/hello")
    class Helloworld(Resource):
        def get(self):
            return jsonify("hello world")

    return app