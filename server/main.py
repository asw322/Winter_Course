'''
main.py is the business application layer that interacts with the underlying data layer (database)
to fulfill a client's REST requests
'''

from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from modules.api import *

app = Flask(__name__, static_url_path='', static_folder='../client/build')

@app.route('/')
def home():
    return "Hello World"

'''
Write the Create operation to insert users into your database
'''
#########################################
## INSERT YOUR CODE HERE
@app.route('/insert/<username>')
def insertUser(username):
    return "inserting a user: %s" % username
#########################################

'''
Write the Delete operation to delete users in your database
'''
#########################################
## INSERT YOUR CODE HERE
#########################################

'''
Write the Search operation to search users in your database
'''
#########################################
## INSERT YOUR CODE HERE
#########################################

'''
Write the Replace operation to replace users' information in your database
'''
#########################################
## INSERT YOUR CODE HERE
#########################################

'''
Create CRUD operations to handle posts
'''





'''

'''

if __name__ == '__main__':
    app.run()