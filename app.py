# *** Imports Flask                 
from flask import Flask
app = Flask(__name__)

# *** Index route
@app.route('/')
def index(): 
    return 'Hello, this is PetFax!'
