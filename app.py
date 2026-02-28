from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# this is what we were doing in mad1
# @app.route('/')
# def index():
#     return rendered_template('index.html')

# this is what we are doing in mad2, i.e creating api
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Get method received'}
    def post(self):
        return {'message': 'Post method received'}
    def put(self):
        return {'message': 'Put method received'}
    def patch(self):
        return {'message': 'Patch method received'}
    def delete(self):
        return {'message': 'Delete method received'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)