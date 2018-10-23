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


def MarvelCharacters():
    # Maken van de API Url

    timestamp = time.time()
    publicApiKey = 'ce72ea27bb97e27dbf4b8be2decb44ee'
    privateApiKey = 'dfaa8dfee51de0c124a3ee2b4bd8e6d15ba1b4fa'
    stringToHash = str(timestamp) + privateApiKey + publicApiKey
    hash_object = hashlib.md5(stringToHash.encode())
    md5Hash = hash_object.hexdigest()
    apiUrl = 'http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}'.format(timestamp, publicApiKey, md5Hash)
    print(apiUrl)   # deze moet op gegeven moment uit de code weggehaald worden
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

    for character in allCharacters:
        charlst.append(character['name'])  # add char to char list
        descriplst.append(character['description'])  # add descrip to descrip list

    randomselect = random.choice(charlst)  # select random char

    while True:
        descriptionchar = descriplst[charlst.index(randomselect)]
        if len(descriptionchar) >= 1:  # if descrip of selected char >1 let prog know
            print('{}'.format(randomselect))
            break
        else:                                                 # if descrip of selected char non exist let prog know
            randomselect = random.choice(charlst)

    charpic = character["thumbnail"]["path"] + character["thumbnail"]["extension"]
    return {'character': randomselect, 'description': descriptionchar, 'charthumbnail': charpic}  # return character and descrip for later use


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

    for row in c.execute("SELECT * FROM highscore"):
        print(row)

    conn.close()

# start programma
print('quiz gestart')
name = input('Wat is je naam: ')
allCharacters = MarvelCharacters()
chosenCharacter = chooseCharacter(allCharacters)
# hints eerst uit discription halen van de gekozen character
#import time module for sleep


punten = 25

while True:
    if punten >= 1:  # The player should have at least one point to start the test.
        character = input('a  b  c  d')  # If the first answer was correct, player can answer this question.
        if character == 'c':
            print('Correct! you\'ve earned ' + str(punten) + ' points')
            punten = punten+25
            print('Your total amount of points accumilates to ' + str(punten) + ' points')
            saveScore(name, punten)
            break
        elif character == 'hint':
            punten = punten - 3
            print(giveHint(chosenCharacter))
        else:
            punten = punten - 1  # The player losses one point by clicking on wrong answer.
            print('Wrong! you\'re points have gone down to ' + str(punten))
    else:
        print("Gameover")
        break

loadHighScore()
