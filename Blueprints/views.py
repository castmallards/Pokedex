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
    is_valid = True

    malicious_strings = ['INSERT', 'ADD','CREATE', 'DELETE', 'WHERE','DROP','SELECT', 'INSERT', '=', '*', '--', '<', '>']

    for row in malicious_strings:
        if(row in input_str):
            is_valid = False

    return is_valid

@views.route('/hasAbility')
def hasAbility_page():
    curr = conn.cursor()
    all_pk_abilities = 'SELECT * FROM Has_ability'
    curr.execute(all_pk_abilities)
    result = curr.fetchall()
    return render_template("hasAbility.html", hasAbility=result)

@views.route('/trainers')
def trainers_page():
    curr = conn.cursor()
    all_trainers = 'SELECT * FROM Trainers'
    curr.execute(all_trainers)
    result = curr.fetchall()
    return render_template("trainers.html", Trainers=result)

@views.route('/bosses')
def bossess_page():
    curr = conn.cursor()
    all_bosses = 'SELECT * FROM Bosses'
    curr.execute(all_bosses)
    result = curr.fetchall()
    return render_template("bosses.html", Bosses=result)

@views.route('/types')
def types_page():
    curr = conn.cursor()
    all_types = 'SELECT * FROM Types'
    curr.execute(all_types)
    result = curr.fetchall()
    return render_template("types.html", Types=result)

@views.route('/hasType')
def hasType_page():
    curr = conn.cursor()
    has_type = 'SELECT * FROM Has_Type'
    curr.execute(has_type)
    result = curr.fetchall()
    return render_template("hasType.html", hasType=result)

@views.route('/roster')
def roster_page():
    curr = conn.cursor()
    roster = 'SELECT * FROM Roster'
    curr.execute(roster)
    result = curr.fetchall()
    return render_template("roster.html", Roster=result)

@views.route('/evolutions')
def evolutions_page():
    curr = conn.cursor()
    all_evolutions = 'SELECT p1.pok_name, p2.pok_name, p3.pok_name FROM Pokemon p1 LEFT JOIN Pokemon p2 ON p2.evolves_from = p1.nat_id LEFT JOIN Pokemon p3 ON p3.evolves_from = p2.nat_id ORDER BY p1.pok_name;'
    curr.execute(all_evolutions)
    result = curr.fetchall()
    return render_template("evolutions.html", Evolutions=result)

@views.route('/allAbilities')
def all_abilities_page():
    curr = conn.cursor()
    first_cte = 'WITH primaries AS ( SELECT Pokemon.nat_id, Has_ability.ability_name FROM Pokemon JOIN Has_ability ON Pokemon.nat_id = Has_ability.nat_id WHERE Has_ability.ability_type = \'primary\'),'
    second_cte = 'secondaries AS ( SELECT Pokemon.nat_id, Has_ability.ability_name FROM Pokemon JOIN Has_ability ON Pokemon.nat_id = Has_ability.nat_id WHERE Has_ability.ability_type = \'secondary\'),'
    third_cte = 'hiddens AS ( SELECT Pokemon.nat_id, Has_ability.ability_name FROM Pokemon JOIN Has_ability ON Pokemon.nat_id = Has_ability.nat_id WHERE Has_ability.ability_type = \'hidden\') '
    all_abilities = first_cte + second_cte + third_cte + 'SELECT Pokemon.nat_id, Pokemon.pok_name,primaries.ability_name, secondaries.ability_name, hiddens.ability_name FROM Pokemon LEFT JOIN primaries ON Pokemon.nat_id = primaries.nat_id LEFT JOIN secondaries ON Pokemon.nat_id = secondaries.nat_id LEFT JOIN hiddens ON Pokemon.nat_id = hiddens.nat_id ORDER BY Pokemon.nat_id;'
    curr.execute(all_abilities)
    result = curr.fetchall()
    return render_template("allAbilities.html", AllAbilites=result)