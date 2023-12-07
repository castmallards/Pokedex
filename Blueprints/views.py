from flask import Blueprint, request
from flask.templating import render_template
# from . import conn

# :param: 
# -- 'views' is name of file
# -- template_folder = the template directory where all the routes/templates are 
views = Blueprint('views', __name__, template_folder="templates")

# Home page with some info and intro
@views.route('/')
def homepage():
    return render_template("homepage.html")


# Pokemon page shows a list of pokemons
@views.route('/pokemon')
def pokemon_page():
    return render_template("pokemon.html")

@views.route('/moves')
def moves_page():
    return render_template("moves.html")