# *** Imports the flask package as Flask
from flask import Flask

# * Defines function that will be the application factory
def create_app():
    # * App instance of flask
    app = Flask(__name__)

    # * Basic index route that goes to '/' and returns 'Hello...'
    @app.route('/')
    def hello():
        return "Hello, PetFax! 🐶"
    
    return app