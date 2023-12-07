#This python file is used for creating an SQL file which will clean up previous 
#tables (product), clean up current tables (our tables), make create statements for
#new tables (our tables) and create insert statements for said tables.

import csv
import re
import os
###########################################################################################################################################

def dropTablesAndSetup(sqlFileName):
    if(sqlFileName):
       #always start the beginning of file
       open(sqlFileName, "w").close()

       sqlWriter = open(sqlFileName, "a")

       sqlWriter.write("--Specifying use case\n")
       sqlWriter.write("use cs3380;\n\n")

       sqlWriter.write("--Cleaning up previous tables;\n")
       sqlWriter.write("DROP TABLE IF EXISTS viewed;\n")
       sqlWriter.write("DROP TABLE IF EXISTS orders;\n")
       sqlWriter.write("DROP TABLE IF EXISTS people;\n")
       sqlWriter.write("DROP TABLE IF EXISTS orderLineItems;\n")
       sqlWriter.write("DROP TABLE IF EXISTS products;\n")
       sqlWriter.write("DROP TABLE IF EXISTS provinces;\n\n")
       
       sqlWriter.write("--Cleaning up current tables;\n")
       sqlWriter.write("DROP TABLE IF EXISTS Roster;\n")
       sqlWriter.write("DROP TABLE IF EXISTS Bosses;\n")
       sqlWriter.write("DROP TABLE IF EXISTS Effect;\n")
       sqlWriter.write("DROP TABLE IF EXISTS Has_type;\n")
       sqlWriter.write("DROP TABLE IF EXISTS Has_ability;\n")
       sqlWriter.write("DROP TABLE IF EXISTS Pokemon;\n") 
       sqlWriter.write("DROP TABLE IF EXISTS Moves;\n") 
       sqlWriter.write("DROP TABLE IF EXISTS Trainers;\n") 
       sqlWriter.write("DROP TABLE IF EXISTS Abilities;\n") 
       sqlWriter.write("DROP TABLE IF EXISTS Types;\n") 
       sqlWriter.write("DROP TABLE IF EXISTS Games;\n\n") 

       sqlWriter.close()



def createTables(sqlFileName):
    if(sqlFileName):
        
        sqlWriter = open(sqlFileName, "a")

        sqlWriter.write("--Creating new tables\n")

        gamesTableStr = "CREATE TABLE Games (game_name VARCHAR(100) NOT NULL, release_year INT NOT NULL, PRIMARY KEY (game_name));\n"
        typesTableStr = "CREATE TABLE Types (type_name VARCHAR(100) NOT NULL, PRIMARY KEY (type_name));\n"
        abilitiesTableStr = "CREATE TABLE Abilities (ability_name VARCHAR(100) NOT NULL, description VARCHAR(200), orig_gen INT NOT NULL, PRIMARY KEY (ability_name));\n"
        trainersTableStr = "CREATE TABLE Trainers (trainer_name VARCHAR(100) NOT NULL, PRIMARY KEY (trainer_name));\n"
        movesTableStr = "CREATE TABLE Moves (move_name VARCHAR(100) NOT NULL, move_type VARCHAR(100) NOT NULL REFERENCES Types(type_name), move_power INT NOT NULL, move_acc INT NOT NULL, move_pp INT NOT NULL, orig_gen INT NOT NULL, PRIMARY KEY (move_name));\n"
        pokemonTableStr = "CREATE TABLE Pokemon (nat_id INT NOT NULL, pok_name VARCHAR(100) NOT NULL, orig_game VARCHAR(100) NOT NULL REFERENCES Games(game_name), evolves_from INT REFERENCES Pokemon(nat_id), hp INT NOT NULL, attack INT NOT NULL, defense INT NOT NULL, PRIMARY KEY (nat_id));\n"
        hasAbilityTableStr = "CREATE TABLE Has_ability (nat_id INT NOT NULL REFERENCES Pokemon(nat_id), ability_name VARCHAR(100) NOT NULL, ability_type VARCHAR(100) NOT NULL, PRIMARY KEY (nat_id, ability_name));\n"
        hasTypeTableStr = "CREATE TABLE Has_Type (nat_id INT NOT NULL REFERENCES Pokemon(nat_id), type_name VARCHAR(100) NOT NULL REFERENCES Types(type_name), PRIMARY KEY (nat_id, type_name));\n"
        effectTableStr = "CREATE TABLE Effect (affecting_type VARCHAR(100) NOT NULL REFERENCES Types(type_name), affected_type VARCHAR(100) NOT NULL REFERENCES Types(type_name), effect_level INT NOT NULL, PRIMARY KEY (affecting_type, affected_type));\n"
        bossesTableStr = "CREATE TABLE Bosses (boss_name VARCHAR(100) NOT NULL REFERENCES Trainers(trainer_name), boss_game VARCHAR(100) NOT NULL REFERENCES Games(game_name), PRIMARY KEY (boss_name, boss_game));\n"
        rosterTableStr = "CREATE TABLE Roster (roster_entry_id INT IDENTITY(1,1) PRIMARY KEY, trainer_name VARCHAR(100) NOT NULL REFERENCES Trainers(trainer_name), nat_id INT NOT NULL REFERENCES Pokemon(nat_id), game_name VARCHAR(100) NOT NULL REFERENCES Games(game_name));\n"

        sqlWriter.write(gamesTableStr)
        sqlWriter.write(typesTableStr)
        sqlWriter.write(abilitiesTableStr)
        sqlWriter.write(trainersTableStr)
        sqlWriter.write(movesTableStr)
        sqlWriter.write(pokemonTableStr)
        sqlWriter.write(hasAbilityTableStr)
        sqlWriter.write(hasTypeTableStr)
        sqlWriter.write(effectTableStr)
        sqlWriter.write(bossesTableStr)
        sqlWriter.write(rosterTableStr)
        sqlWriter.write("\n")
        sqlWriter.close()

def gamesInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Games table inserts\n")
        with open(csvFileName, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader, None) #skip header
            for row in reader:
                if(row):
                    sqlWriter.write("INSERT INTO Games(game_name, release_year) VALUES('" + row[0].lower() + "', " + row[1] + ");\n")
            sqlWriter.write("\n")
        sqlWriter.close()  

def typesInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Types table inserts\n")
        with open(csvFileName, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader, None) #skip header
            for row in reader:
                if(row):
                    sqlWriter.write("INSERT INTO Types(type_name) VALUES('" + row[0].lower() + "');\n")
            sqlWriter.write("\n")
        sqlWriter.close() 

def abilitiesInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Abilities table inserts\n")
        with open(csvFileName, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader, None) #skip header
            for row in reader:
                if(row):
                    #clean up quotation marks
                    adj_name = re.sub("'", "''", row[0])
                    adj_name = re.sub('"', '', adj_name)
                    adj_desc = re.sub("'", "''", row[2])
                    adj_desc = re.sub('"', '', adj_desc)
                    
                    sqlWriter.write("INSERT INTO Abilities(ability_name, description, orig_gen) VALUES('" + adj_name.lower() + "', '" + adj_desc+ "', " + row[3] + ");\n")
            sqlWriter.write("\n")
            sqlWriter.close()

def movesInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Moves table inserts\n")
        with open(csvFileName, 'r') as csvFile:
            reader = csv.reader(csvFile)
            next(reader, None) #skip header
            for row in reader:
                if(row):
                    #clean up quotation marks
                    adj_name = re.sub("'", "''", row[0])
                    adj_name = re.sub('"', '', adj_name)

                    #filter rows with missing cols (not in line with our model)
                    if(len(row) == 8): 
                        sqlWriter.write("INSERT INTO Moves(move_name, move_type, move_power, move_acc, move_pp, orig_gen) VALUES('" + adj_name.lower() + "', '" + row[1].lower() + "', " + row[3] + ", " + row[4] + ", " + row[5] + ", " + row[7] + ");\n") 
            sqlWriter.write("\n")
            csvFile.close()
            sqlWriter.close()


def getNatIDFromLocalID(localID, csvFilename):
    #NULL string comes from CSV file
    if(localID and csvFilename and localID != 'NULL'):
        with open(csvFilename, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if(row[0] == localID):
                    id = row[1]
                    csvFile.close() 
                    return id
        csvFile.close()    

def getNatIDFromName(pokemonName, csvFilename):
    if(pokemonName and csvFilename):
        with open(csvFilename, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                name = re.sub('"', '', row[2])
                name = re.sub("'", "''", name)
                name = name.lower()
                if(name == pokemonName):
                    id = row[1]
                    csvFile.close() 
                    return id
        csvFile.close()    



def pokemonInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Pokemon inserts here\n")
        with open(csvFileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader, None) #skip header
            #Keep list of pokemon inserted to filter duplicates. 
            #Duplicate entries are outside the scope of the model.
            natIDList = [] 
            for row in csvReader:
                #row[4] helps filter special case pokemon (same as above)
                #filter duplicates and special cases
                if(row and row[4] == 'NULL' and row[1] not in natIDList): 
                    nat_id = row[1]
                    natIDList.append(nat_id) #append to list if found
                    #clean up quotes
                    pok_name = re.sub('"', "", row[2])
                    pok_name = re.sub("'", "''", pok_name)
                    pok_name = "'" + pok_name + "'" #add quotes for ease
                    orig_game = re.sub('"', "", row[22])
                    orig_game = "'" + orig_game + "'" #add quotes for ease
                    evolvesFrom = getNatIDFromLocalID(row[43], csvFileName)
                    hp = row[23]
                    attack = row[24]
                    defense = row[25]
                    
                    if(evolvesFrom):
                        sqlWriter.write("INSERT INTO Pokemon(nat_id, pok_name, orig_game, evolves_from, hp, attack, defense) VALUES(" + nat_id + ", " + pok_name.lower() + ", " + orig_game.lower() + ", " + evolvesFrom + ", " + hp + ", " + attack + ", " + defense + ");\n")
                    else:
                        sqlWriter.write("INSERT INTO Pokemon(nat_id, pok_name, orig_game, hp, attack, defense) VALUES(" + nat_id + ", " + pok_name.lower() + ", " + orig_game.lower() + ", " + hp + ", " + attack + ", " + defense + ");\n")
            sqlWriter.write("\n")
            csvFile.close()
            sqlWriter.close()

def has_abilityInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Has_ability inserts here\n")  
        with open(csvFileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader, None) 
            natIDList = [] #same filtering technique as before
            for row in csvReader:
                #same filtering technique as before
                if(row and row[1] not in natIDList and row[4] == 'NULL'):
                    nat_id = row[1]
                    natIDList.append(nat_id) #append as before
                    primary_ability = re.sub('"', "", row[11])
                    primary_ability = re.sub("'", "''", primary_ability)
                    second_ability = re.sub('"', "", row[13])
                    second_ability = re.sub("'", "''", second_ability)
                    hidden_ability = re.sub('"', "", row[15])
                    hidden_ability = re.sub("'", "''", hidden_ability)

                    if(primary_ability != 'NULL'):
                        sqlWriter.write("INSERT INTO Has_ability(nat_id, ability_name, ability_type) VALUES(" + nat_id + ", '" + primary_ability.lower() + "', 'primary');\n")
                    if(second_ability != 'NULL'):
                        sqlWriter.write("INSERT INTO Has_ability(nat_id, ability_name, ability_type) VALUES(" + nat_id + ", '" + second_ability.lower() + "', 'secondary');\n")
                    if(hidden_ability != 'NULL'):
                        sqlWriter.write("INSERT INTO Has_ability(nat_id, ability_name, ability_type) VALUES(" + nat_id + ", '" + hidden_ability.lower() + "', 'hidden');\n")
            sqlWriter.write("\n")
            csvFile.close()
            sqlWriter.close()

       
def has_typeInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Has_type inserts here\n")  
        with open(csvFileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader, None) #skip header
            natIDList = [] #same filtering technique as before
            for row in csvReader:
                #same filtering technique as before  
                if(row and row[1] not in natIDList and row[4] == 'NULL'):
                    nat_id = row[1]
                    natIDList.append(nat_id) #append as before
                    
                    #clean up quotes
                    primary_type = re.sub('"', "", row[9])
                    primary_type = re.sub("'", "''", primary_type)
                    secondary_type = re.sub('"', "", row[10])
                    secondary_type = re.sub("'", "''", secondary_type)

                    if(primary_type != 'NULL'): 
                        sqlWriter.write("INSERT INTO Has_type(nat_id, type_name) VALUES(" + nat_id + ",'" + primary_type.lower() + "');\n")
                    if(secondary_type != 'NULL'):
                        sqlWriter.write("INSERT INTO Has_type(nat_id, type_name) VALUES(" + nat_id + ",'" + secondary_type.lower() + "');\n")
            sqlWriter.write("\n")
            csvFile.close()
            sqlWriter.close()


def effectInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Effect inserts here\n")  
        with open(csvFileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader, None) #skip header  
            for row in csvReader:
                    if(row):
                        affecting_type = "'" + row[0].lower() + "'"
                        affected_type =  "'" + row[1].lower() + "'"
                        level = row[2]
                        sqlWriter.write("INSERT INTO Effect(affecting_type, affected_type, effect_level) VALUES(" + affecting_type + ", " + affected_type + ", " + level +");\n")   
            sqlWriter.write("\n")
            csvFile.close()
            sqlWriter.close()


def trainerInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        namesIncluded = [] #similar filtering for duplicates as before
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Trainers inserts here\n")  
        with open(csvFileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            next(csvReader, None) #skip header     
            for row in csvReader:
                if(row and row[3].lower() not in namesIncluded):
                    name = "'" + row[3].lower() + "'"
                    namesIncluded.append(row[3].lower()) #append to list as before
                    sqlWriter.write("INSERT INTO Trainers(trainer_name) VALUES(" + name + ");\n")
            sqlWriter.write("\n")
            csvFile.close()
            sqlWriter.close()


def bossesInserts(sqlFileName, csvFileName):
    if(sqlFileName and csvFileName):
        bossList = [] #as before, keep list to filter duplicates
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Bosses inserts here\n")  
        with open(csvFileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            next(csvReader, None) #skip header 
        
            for row in csvReader:
                if(row):
                 
                    boss_name = row[3].lower()
                    boss_game = row[1].lower()  
  
                    tuple = [] 
                    tuple.append(boss_name)
                    tuple.append(boss_game) 

                    if(tuple not in bossList):
                        bossList.append(tuple) #append as before
                        boss_name = "'" + boss_name + "'"
                        boss_game = "'" + boss_game + "'"  
                        sqlWriter.write("INSERT INTO Bosses(boss_name, boss_game) VALUES (" + boss_name + ", " + boss_game + ");\n")

            sqlWriter.write("\n")
            csvFile.close()
            sqlWriter.close()

def rosterInserts(sqlFileName, csvFileName, pokemonCSV):
    if(sqlFileName and csvFileName):
        sqlWriter = open(sqlFileName, "a")
        sqlWriter.write("--Roster inserts here\n")  
        with open(csvFileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=';')
            next(csvReader, None) #skip header 
        
            for row in csvReader:
                if(row):
                    boss_name = row[3].lower()
                    boss_game = row[1].lower() 
                    boss_name = "'" + boss_name + "'"
                    boss_game = "'" + boss_game + "'"
                    name = re.sub("'", "''", row[4])
                    name = re.sub('"', '', name)
                    name = name.lower()
                    nat_id = getNatIDFromName(name, pokemonCSV)
                    sqlWriter.write("INSERT INTO Roster(trainer_name, nat_id, game_name) VALUES(" + boss_name + ", " + nat_id + ", " + boss_game + ");\n")
            sqlWriter.write("\n")
            csvFile.close()
            sqlWriter.close()
                     

def init():
    path = os.path.realpath(__file__)
    dir = os.path.dirname(path)
    os.chdir(dir)

    sqlFileName = 'Pokemon.sql'
    pokemonCSV = 'Pokemon Database.csv'
    gamesCSV = 'AllGames.csv'
    typesCSV = 'AllTypes.csv'
    abilitiesCSV = 'abilities.csv'
    movesCSV = 'Moves.csv'
    effectsCSV = 'AllEffects.csv'
    bossesCSV = 'PokemonGymLeaders.csv'

    dropTablesAndSetup(sqlFileName)

    createTables(sqlFileName)

    gamesInserts(sqlFileName, gamesCSV)

    typesInserts(sqlFileName, typesCSV)

    abilitiesInserts(sqlFileName, abilitiesCSV)

    movesInserts(sqlFileName, movesCSV)

    pokemonInserts(sqlFileName, pokemonCSV)

    has_abilityInserts(sqlFileName, pokemonCSV)

    has_typeInserts(sqlFileName, pokemonCSV)

    effectInserts(sqlFileName, effectsCSV)

    trainerInserts(sqlFileName, bossesCSV)

    bossesInserts(sqlFileName, bossesCSV)

    rosterInserts(sqlFileName, bossesCSV, pokemonCSV)
###########################################################################################################################################

init()


