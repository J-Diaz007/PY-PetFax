# *** Imports the blueprint class and render_template
from flask import ( Blueprint, render_template )


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
    return render_template ('index.html')