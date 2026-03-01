from flask_restful import Resource, Api
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

api = Api()

from models import User, db

# this is what we were doing in mad1
# @app.route('/')
# def index():
#     return rendered_template('index.html')

# this is what we are doing in mad2, i.e creating api

### Auth endpoints
class Login(Resource):
    def post(self):
        data = request.get_json()
        if 'email' not in data or 'password' not in data:
            return {'message': 'Email and password are required'}, 400
        user = User.query.filter_by(email=data['email']).first()
        if not user or user.password != data['password']:
            return {'message': 'Invalid email or password'}, 401
        # user is authenticated, create JWT token
        token = create_access_token(identity=user.email)
        return {
            'message': f'Successfully logged in as {user.name}', 
            'token': token,
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role
            }
        }, 200
api.add_resource(Login, '/login')
    
class Register(Resource):
    def post(self):
        data = request.get_json()
        if 'name' not in data or 'email' not in data or 'password' not in data:
            return {'message': "name, email, and password are required"}, 400
        
        user = User.query.filter_by(email=data['email']).first()
        if user:
            return {'message': 'User with this email already exists'}, 400

        new_user = User(name=data['name'], email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()

        user_dict = {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email,
            'role': new_user.role
        }

        return {'message': f'Successfully registered user with id {new_user.id}', 'user': user_dict}, 201
api.add_resource(Register, '/register')

    
### Admin endpoits
class Users_info(Resource):
    @jwt_required()
    def get(self, user_id=None):
        if user_id is not None:
            user = User.query.get(user_id)
            if not user:
                return {'message': f'User with id {user_id} does not exist'}, 404
            user_dict = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role
            }
            return {
                "message": f'Successfully retrieved user with id {user_id}',
                "user": user_dict
            }, 200
        users = User.query.all()
        users_list = []
        for user in users:
            user_dict = {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'role': user.role
            }
            users_list.append(user_dict)
        return {
            'message': 'Successfully retrieved all users',
            'users': users_list
        }, 200
    
    @jwt_required()
    def post(self):
        current_user = User.query.filter_by(email=get_jwt_identity()).first()
        if not current_user or current_user.role != 'admin':
            return {'message': 'You do not have permission to create a new user'}, 403

        data = request.get_json()
        print('Received data:', data)

        if 'name' not in data or 'email' not in data or 'password' not in data:
            return {'message': "name, email, and password are required"}, 400
        
        user = User.query.filter_by(email=data['email']).first()
        if user:
            return {'message': 'User with this email already exists'}, 400

        new_user = User(name=data['name'], email=data['email'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()

        user_dict = {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email,
            'role': new_user.role
        }

        return {'message': f'Successfully created user with id {new_user.id}', 'user': user_dict}, 201
    
    @jwt_required()
    def put(self, user_id=None):
        if user_id is None:
            return {'message': 'user_id is required'}, 400
        data = request.get_json()
        user = User.query.get(user_id)
        if not user:
            return {'message': f'User with id {user_id} does not exist'}, 404
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            is_email_taken = User.query.filter_by(email=data['email']).first()
            if is_email_taken and is_email_taken.id != user_id:
                return {'message': 'Email is already taken by another user'}, 400
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']
        db.session.commit()
        return {'message': f'Successfully updated user with id {user_id}', 'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        }}, 200
    
    @jwt_required()
    def delete(self, user_id=None):
        if user_id is None:
            return {'message': 'user_id is required'}, 400
        print(f'Received request to delete user with id: {user_id}')
        user = User.query.get(user_id)
        if not user:
            return {'message': f'User with id {user_id} does not exist'}, 404
        db.session.delete(user)
        db.session.commit()
        return {'message': f'Successfully deleted user with id {user_id}'}, 200

api.add_resource(Users_info, '/users', '/users/<int:user_id>')


### User endpoints


