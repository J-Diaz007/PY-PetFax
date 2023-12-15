# *** Imports the blueprint class and render_template
from flask import ( Blueprint, render_template )

# Imports json since our data is in a JSON file format and not in a database
import json

# * Built in functions open() and json.load()
# Passes pets.json file as an argument in the open() function to "open the file".
# Entire function then needs to be passed inside json.load() function as an argument to be readable
# * open() "opens files" and json.load() "decodes JSON data"
pets = json.load(open('pets.json'))
print(pets)

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
    return render_template (
        'pets/index.html',
        pets=pets,
        )

@bp.route('/<int:id>')
def show(id):
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)