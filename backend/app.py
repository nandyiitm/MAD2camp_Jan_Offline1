from flask import Flask, request

app = Flask(__name__)

# enabling CORS for all routes and origins
from flask_cors import CORS
CORS(app)

# config db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
from models import db, User
db.init_app(app)

# jwt config
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
from flask_jwt_extended import JWTManager
jwt = JWTManager(app)

# config routes
from routes import api, cache
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 30
cache.init_app(app)  # Initialize cache with the Flask app
api.init_app(app)    # initialize api with the Flask app

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

        admin = User.query.filter_by(email='admin@gmail.com').first()
        if not admin:
            admin = User(name='Admin User', email='admin@gmail.com', role='admin', password='1234')
            db.session.add(admin)
            db.session.commit()

            print('Admin user created with email: admin@gmail.com and password: 1234')
    
    app.run(debug=True)