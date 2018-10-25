import time
import hashlib
import json
import random
import requests  # pip install requests uitvoeren in Terminal om te installeren voor de 1e keer
import sqlite3


#def setTimer(ans):
#    # set initial timer value
#    timer = 90
#    # anwser not yet filled in
#    while ans == '' and timer >= 1:
#        timer = timer-1
#        time.sleep(1)
#    # the right anwser, timer reset
#    if ans:
#        return ans
#    # timer ran out, anwser is wrong.
#    elif timer <= 0:
#        ans = False
#    return ans


def MarvelCharacters(offset):
    # Maken van de API Url

    timestamp = time.time()
    publicApiKey = 'ce72ea27bb97e27dbf4b8be2decb44ee'
    privateApiKey = 'dfaa8dfee51de0c124a3ee2b4bd8e6d15ba1b4fa'
    stringToHash = str(timestamp) + privateApiKey + publicApiKey
    hash_object = hashlib.md5(stringToHash.encode())
    md5Hash = hash_object.hexdigest()
    apiUrl = 'http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit=10&offset={}'.format(timestamp, publicApiKey, md5Hash, offset)
    #print(apiUrl)   # deze moet op gegeven moment uit de code weggehaald worden
    # voorbeeld voor hoe het eruit komt te zien en deze kun je dan in Visual Studio Code gebruiken
    # http://gateway.marvel.com/v1/public/characters?ts=1539531767.861436&apikey=ce72ea27bb97e27dbf4b8be2decb44ee&hash=1efc26ce5b2905641dd9413bfe6662d8

    # Aanroepen van API Url
    response = requests.get(apiUrl)

    # Resultaten van API in Json omzetten naar dictionary
    apiResults = json.loads(response.text)

    # Alle characters uitlezen uit API
    allCharacters = apiResults['data']['results']

    return allCharacters






def chooseCharacter(apilst):
    allCharacters = apilst  # read api list
    charlst = []  # create fresh list for char names
    descriplst = []  # create fresh list for descriptions
    imagelst = []

    for character in allCharacters:
        charlst.append(character['name'])  # add char to char list
        descriplst.append(character['description'])  # add descrip to descrip list
        imagelst.append(character["thumbnail"]["path"] + '.' + character["thumbnail"]["extension"])

    randomselect = random.choice(charlst)  # select random char



    while True:
        descriptionchar = descriplst[charlst.index(randomselect)]
        imageUrl = imagelst[charlst.index(randomselect)]
        if len(descriptionchar) >= 1:  # if descrip of selected char >1 let prog know
            break
        else:                                                 # if descrip of selected char non exist let prog know
            randomselect = random.choice(charlst)

    return {'character': randomselect, 'description': descriptionchar, 'imageUrl': imageUrl}  # return character and descrip for later use

#make a list of 4 superhero's to be used in the quiz as options


def options(apilst,chosenCharacter):
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
    conn = sqlite3.connect('highscore.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS highscore
               (date DATETIME, name TEXT, score INT)''')

    c.execute("INSERT INTO highscore VALUES (date('now'),?,?)", (name, score))

    conn.commit()
    conn.close()


def loadHighScore():
    conn = sqlite3.connect('highscore.db')
    c = conn.cursor()
    highscore = ''

    for row in c.execute("SELECT * FROM highscore"):
        highscore = highscore + "{} {} {}\n".format(row[0], row[1], row[2])
    return highscore

# start programma


# hints eerst uit discription halen van de gekozen character
#import time module for sleep


def point_calc(ans,points):
    global gameover
    if ans == True and points > 0:
        points = points+25
        saveScore(name, points)
        gameover = False
    elif ans == False and points > 0:
        points = points - 10
        gameover = False
    elif points <= 0:
        gameover = True
    return points

#loadHighScore()