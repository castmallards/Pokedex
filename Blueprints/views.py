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

@views.route('/newPkmnIntro')
def newPkmnIntro_page():
    # query = ""
    # if request.method == "POST":
    #     game = request.form['Games']
    #     if game == 'None':
    #         query = ""
    #     else: # Check for SQL injection 
    #         query =  game
    # else:
    #     query = ""
    curr = conn.cursor()
    curr.execute('SELECT game_name FROM Games')
    game_list = curr.fetchall()
    return render_template('newPkmnIntro.html', Games=game_list)

@views.route('/newPkmnIntro/<game_name>')
def newPkmnInfoResult_page(game_name):

    #check  = validat_injection(game_name)
    # if check:
    game = game_name
    curr = conn.cursor()
    query = 'SELECT Has_Type.type_name, count(*) as numIntroduced FROM Has_Type LEFT JOIN Pokemon ON Pokemon.nat_id = Has_Type.nat_id WHERE Pokemon.orig_game = \'{}\' GROUP BY Has_Type.type_name ORDER BY numIntroduced DESC;'.format(game)
    curr.execute(query)
    types = curr.fetchall()
    print(types)

    return render_template('newPknmIntro_result.html', Type=types)