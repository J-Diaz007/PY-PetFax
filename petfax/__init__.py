# *** Imports the flask package as Flask
from flask import Flask

# * Defines a function that will be the application factory
def create_app():
    # * App instance of flask
    app = Flask(__name__)

    # * Basic index route that goes to '/' and returns 'Hello...'
    @app.route('/')
    def index():
        return "Hello, PetFax! 🐶"

    #Tegisters the pet blueprint
    from . import pet
    # Calls the register_blueprint method on the app instance and passes the pet blueprint into the method
    app.register_blueprint(pet.bp)

     # Registers the fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    return app