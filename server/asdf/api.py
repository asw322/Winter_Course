from flask_restful import Api, Resource, reqparse

class UserApiHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': 'Hello from User API Handler'
        }

    def insertUser():
        '''
        Write the create operation to insert users into your database
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        return {
            'resultStatus': None,
            'message': None
        }
        #########################################

    def deleteUser():
        '''
        Write the delete operation to delete users from your database
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        return {
            'resultStatus': None,
            'message': None
        }
        #########################################

    def searchUser():
        '''
        Write the search operation to search users from your database
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        return {
            'resultStatus': None,
            'message': None
        }
        #########################################

    def deleteUser():
        '''
        Write the delete operation to delete users from your database
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        return {
            'resultStatus': None,
            'message': None
        }
        #########################################

    
        

    
class PostApiHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': 'Hello from User API Handler'
        }