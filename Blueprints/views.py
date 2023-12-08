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


@views.route('/newPkmnIntro')
def newPkmnIntro_page():
    curr = conn.cursor()
    curr.execute('SELECT game_name FROM Games')
    game_list = curr.fetchall()
    return render_template('newPkmnIntro.html', Games=game_list)

@views.route('/newPkmnIntro/<game_name>')
def newPkmnInfoResult_page(game_name):
    #check  = validat_injection(game_name)
    types = ""
    if validate_input(game_name):
        game = game_name
        curr = conn.cursor()
        query = 'SELECT Has_Type.type_name, count(*) as numIntroduced FROM Has_Type LEFT JOIN Pokemon ON Pokemon.nat_id = Has_Type.nat_id WHERE Pokemon.orig_game = \'{}\' GROUP BY Has_Type.type_name ORDER BY numIntroduced DESC;'.format(game)
        curr.execute(query)
        types = curr.fetchall()
    

    return render_template('newPknmIntro_result.html', Type=types)


@views.route('/moves')
def moves_page():
    curr = conn.cursor()
    all_moves = 'SELECT * FROM Moves'
    curr.execute(all_moves)
    result = curr.fetchall()
    return render_template("moves.html", Moves=result)

@views.route('/abilities')
def abilities_page():
    curr = conn.cursor()
    all_abilities = 'SELECT * FROM Abilities'
    curr.execute(all_abilities)
    result = curr.fetchall()
    return render_template("abilities.html", Abilities=result)

@views.route('/games')
def games_page():
    curr = conn.cursor()
    all_games = 'SELECT * FROM Games'
    curr.execute(all_games)
    result = curr.fetchall()
    return render_template("games.html", Games=result)

@views.route('/effect')
def effect_page():
    curr = conn.cursor()
    all_effects = 'SELECT * FROM Effect'
    curr.execute(all_effects)
    result = curr.fetchall()
    return render_template("effect.html", Effect=result)

def validate_input(input_str):
    return True

@views.route('/hasAbility')
def hasAbility_page():
    curr = conn.cursor()
    all_pk_abilities = 'SELECT * FROM Has_ability'
    curr.execute(all_pk_abilities)
    result = curr.fetchall()
    return render_template("hasAbility.html", hasAbility=result)

@views.route('/types')
def types_page():
    curr = conn.cursor()
    all_types = 'SELECT * FROM Types'
    curr.execute(all_types)
    result = curr.fetchall()
    return render_template("types.html", Types=result)