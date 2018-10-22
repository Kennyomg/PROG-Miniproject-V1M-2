import time
import hashlib
import json
import random
import requests  # pip install requests uitvoeren in Terminal om te installeren voor de 1e keer


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

    return {'character': randomselect, 'description': descriptionchar}  # return character and descrip for later use


def giveHint(chosenCharacter):
    # chooseCharacter(MarvelCharacters())
    description: str = chosenCharacter["description"]
    filterchardots = chosenCharacter["character"].replace('.','')
    filtercharleftbracket = filterchardots.replace('(', '')
    filtercharrightbracket = filtercharleftbracket.replace(')','')
    filteredchar = filtercharrightbracket.split(' ')
    print(filteredchar)

    # per een pakken, if statement of loop
    while True:
        if len(filteredchar) == 1:
            description.replace(filteredchar[0], "___")
            break
        elif len(filteredchar) > 1:
            index = 0
            index = index + 1
            description.replace(filteredchar[index], "___")
        elif index > len(filteredchar):
            break

    print(description)



# start programma
#print('quiz gestart')
#name = input('Wat is je naam: ')
allCharacters = MarvelCharacters()
chosenCharacter = chooseCharacter(allCharacters)
# hints eerst uit discription halen van de gekozen character
#import time module for sleep

print(giveHint(chosenCharacter))
punten = 25

while True:
    if punten >= 1:  # The player should have at least one point to start the test.
        character = input("Kies het goede antwoord\n 'a', 'b', 'c' of 'd' ")  # If the first answer was correct, player can answer this question.
        if character == 'c':
            print('U hebt de vraag goed beantwoord en u hebt ' + str(punten) + ' score verdient')
            print('Uw totale scoren zijn: ' + str(punten * 2))
            break
        elif character == 'hint':
            punten = punten - 3
            giveHint(chosenCharacter)
        else:
            punten = punten - 1  # The player losses one point by clicking on wrong answer.
            print('Uw antwoord is helaas fout en u hebt nu: ' + str(punten) + ' score.')
            print('Doe het opnieuw:')  # The player can not go to the next question.
    else:
        print("Uw punten zijn op, U heeft verloren")
        break

