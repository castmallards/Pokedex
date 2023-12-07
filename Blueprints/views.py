from flask import Blueprint, request
from flask.templating import render_template
from . import conn 

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
    curr = conn.cursor()
    all_pok = 'SELECT * FROM Pokemon'
    curr.execute(all_pok)
    result = curr.fetchall()

    return render_template("pokemon.html", Pokemon=result)

@views.route('/moves')
def moves_page():
    return render_template("moves.html")

@views.route('/newPkmnIntro', methods=["GET"])
def newPkmnIntro_page():

    if request.method == "GET":
        game = request.form['Games']

    games_list = ''
    types = ''
    curr = conn.cursor()
    curr.execute('SELECT ')

    return render_template('newPkmnIntro.html', Games=games_list, Type=types)

@views.route('/newPkmnIntro/<game_name>', methods=["GET"])
def newPkmnIntro_page():

    if request.method == "GET":
        game = request.form['Games']

    games_list = ''
    types = ''
    curr = conn.cursor()
    curr.execute('SELECT ')

    return render_template('newPkmnIntro_info.html', Games=games_list, Type=types)