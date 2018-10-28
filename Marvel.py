import time
import hashlib
import json
import random
import requests  # pip install requests uitvoeren in Terminal om te installeren voor de 1e keer
import sqlite3


def MarvelCharacters(offset):
    """
    This function will retrieve characters from the marvel api
    :param offset: Offset from starting point of results
    :return: json with Marvel characters
    """

    timestamp = time.time()
    publicApiKey = 'ce72ea27bb97e27dbf4b8be2decb44ee'
    privateApiKey = 'dfaa8dfee51de0c124a3ee2b4bd8e6d15ba1b4fa'
    stringToHash = str(timestamp) + privateApiKey + publicApiKey
    hash_object = hashlib.md5(stringToHash.encode())
    md5Hash = hash_object.hexdigest()
    apiUrl = 'http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=50&offset={}'.format(timestamp, publicApiKey, md5Hash, offset)
    #print(apiUrl)   # deze moet op gegeven moment uit de code weggehaald worden
    # voorbeeld voor hoe het eruit komt te zien en deze kun je dan in Visual Studio Code gebruiken
    # http://gateway.marvel.com/v1/public/characters?ts=1539531767.861436&apikey=ce72ea27bb97e27dbf4b8be2decb44ee&hash=1efc26ce5b2905641dd9413bfe6662d8

    try:
        # Aanroepen van API Url
        print("Trying to do request")
        response = requests.get(apiUrl)
    except requests.exceptions.RequestException as e:
        print(e)

    print("We did it reddit")

    # Resultaten van API in Json omzetten naar dictionary
    apiResults = json.loads(response.text)

    print("Did json conversion")

    # Alle characters uitlezen uit API
    allCharacters = apiResults['data']['results']

    return allCharacters


def chooseCharacter(apilst):
    """
    This function will randomly choose a character
    :param apilst: json with characters from marval api
    :return: Return random chosen character set with character, description and image
    """

    allCharacters = apilst  # read api list
    charlst = []  # create fresh list for char names
    descriplst = []  # create fresh list for descriptions
    imagelst = []

    print("filling lists")
    for character in allCharacters:
        charlst.append(character['name'])  # add char to char list
        descriplst.append(character['description'])  # add descrip to descrip list
        imagelst.append(character["thumbnail"]["path"] + '.' + character["thumbnail"]["extension"])

    print("Choose random character")
    randomselect = random.choice(charlst)  # select random char

    tries = 0
    while True:
        descriptionchar = descriplst[charlst.index(randomselect)]
        imageUrl = imagelst[charlst.index(randomselect)]
        if len(descriptionchar) >= 1:  # if descrip of selected char >1 let prog know
            break
        elif tries < 50:                                                 # if descrip of selected char non exist let prog know
            print("Trying new character")
            tries += 1
            randomselect = random.choice(charlst)
        else:
            descriptionchar = "No hint available... sorry"
            break
    return {'character': randomselect, 'description': descriptionchar, 'imageUrl': imageUrl}  # return character and descrip for later use


def options(apilst,chosenCharacter):
    """
    This function will make a list of 4 superhero's to be used in the quiz as options
    :param apilst: List of all retrieved characters
    :param chosenCharacter: The chosen character
    :return: Returns the options including the correct answer
    """
    allCharacters = apilst
    charlist = []
    options = []
    print(chosenCharacter)
    options.append(chosenCharacter['character'])
    for character in allCharacters:
        charlist.append(character['name'])
    while True:
        if len(options) < 4:
            options.append(random.choice(charlist))
        else:
            random.shuffle(options)
            return options


def giveHint(chosenCharacter):
    """
    This function will give a hint about the character
    :param chosenCharacter: The chosen character
    :return: Returns a part of the description from the chosen character
    """
    # chooseCharacter(MarvelCharacters())
    description: str = chosenCharacter["description"]
    filterchardots = chosenCharacter["character"].replace('.', '')
    filtercharleftbracket = filterchardots.replace('(', '')
    filtercharrightbracket = filtercharleftbracket.replace(')', '')
    filteredchar = filtercharrightbracket.split(' ')

    # per een pakken, if statement of loop
    for i in range(len(filteredchar)):
        description = description.replace(filteredchar[i], "_")

    return description


def saveScore(name: str, score: int):
    """
    This function will save the high score to the sqlite database
    :param name: Highscore user name
    :param score: The highscore
    """

    conn = sqlite3.connect('highscore.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS highscore
               (date DATETIME, name TEXT, score INT)''')

    c.execute("INSERT INTO highscore VALUES (date('now'),?,?)", (name, score))

    conn.commit()
    conn.close()


def loadHighScore():
    """
    This function will get all highscores from the database
    :return: Returns a highscore
    """
    conn = sqlite3.connect('highscore.db')
    c = conn.cursor()
    highscore = ''

    for row in c.execute("SELECT * FROM highscore"):
        highscore = highscore + "{} {} {}\n".format(row[0], row[1], row[2])
    return highscore