# *** Imports Flask                 
from flask import Flask
app = Flask(__name__)

# *** Index route
@app.route('/')
def index(): 
    return 'Hello, this is PetFax! 🐶'

# *** Pets route
@app.route('/pets')
def pets(): 
    return 'These are our pets available for adoption'