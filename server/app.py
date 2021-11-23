'''
app.py is the business application layer that interacts with the underlying data layer (database)
to fulfill a client's REST requests
'''
import sys
sys.path.insert(0, "./asdf")


import os
from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

from api import UserApiHandler

app = Flask(__name__, static_url_path='', static_folder='../client/build')
CORS(app)
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')



api.add_resource(UserApiHandler, '/flask/User')


