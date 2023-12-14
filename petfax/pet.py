# *** Imports the blueprint class
from flask import Blueprint

# * Creates an instance of the blueprint class
bp = Blueprint(
    # Defines the bludeprint name
    'pet',
    # Tell the blueprint where in the project it's defined
    __name__,
    # Defines the blueprint's url prefix
    url_prefix ='/pets'
)

# * Defines a route on the blueprint instance that goes to '/'
@bp.route('/')
# Defines a method for the route named index that returns a string
def index():
    return 'You have reached the pets index =D'