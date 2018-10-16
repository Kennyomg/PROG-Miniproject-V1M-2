import time
import hashlib
import json
import random
import requests
import math


def getAllCharactersFromAPI():
    #Maken van de API Url

    timestamp = time.time()
    publicApiKey = 'ce72ea27bb97e27dbf4b8be2decb44ee'
    privateApiKey = 'dfaa8dfee51de0c124a3ee2b4bd8e6d15ba1b4fa'
    stringToHash = str(timestamp) + privateApiKey + publicApiKey
    hash_object = hashlib.md5(stringToHash.encode())
    md5Hash = hash_object.hexdigest()
    apiUrl = 'http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}&limit={}'.format(timestamp, publicApiKey, md5Hash, 100)

    # voorbeeld voor hoe het eruit komt te zien en deze kun je dan in Visual Studio Code gebruiken
    # http://gateway.marvel.com/v1/public/characters?ts=1539531767.861436&apikey=ce72ea27bb97e27dbf4b8be2decb44ee&hash=1efc26ce5b2905641dd9413bfe6662d8


    # Aanroepen van API Url

    #import requests #pip install requests uitvoeren in Terminal om te installeren voor de 1e keer
    response = requests.get(apiUrl)

    # Resultaten van API in Json omzetten naar dictionary
    apiResults = json.loads(response.text)

    # Alle characters uitlezen uit API
    allCharacters = apiResults['data']['results']

    return allCharacters


def chooseRandomCharacter(allCharacters, excludedCharacter={"name": ""}):
    # Code aanmaken om een character random te kiezen

    randomNumber = random.randrange(0, len(allCharacters))
    print(randomNumber, len(allCharacters))
    chosenCharacter = allCharacters[randomNumber]
    while chosenCharacter["description"] == "" and chosenCharacter["name"] != excludedCharacter["name"]:
        randomNumber = random.randrange(len(allCharacters))
        chosenCharacter = allCharacters[randomNumber]

    return chosenCharacter


def generateHint(chosenCharacter):
    # Code aanmaken om hint te genereren

    description = str(chosenCharacter["description"])
    hint = description.replace(chosenCharacter["name"], "[...]")
    return hint


def checkAnswer(answer, options):
    if options[answer]["correct"]:
        return True
    else:
        return False


def generateOptions(correctCharacter, allCharacters):
    options = [
        {
            "name": correctCharacter["name"],
            "correct": True
        }
    ]

    for i in range(0, 3):
        options.append({
            "name": chooseRandomCharacter(allCharacters)["name"],
            "correct": False
        })

    return options


# start programma
print('quizgestart')
name = input('Wat is je naam: ')
allCharacters = getAllCharactersFromAPI() #Finish
chosenCharacter = chooseRandomCharacter(allCharacters)#nog open #LET OP: Er mag geen Character gekozen worden met een lege discription, daar kunnen we geen hints vandaan halen
print(chosenCharacter)
hint = generateHint(chosenCharacter)# nog open
print(hint)
# hints eerst uit discription halen van de gekozen character

options = generateOptions(chosenCharacter, allCharacters)

print(options)

userInput = input("Druk '1', '2', '3' of '4' voor uw antwoord of voer 'help' in voor een hint")
correct = False

if userInput == 'help':
    print(hint)
elif userInput.isnumeric():
    correct = checkAnswer(int(userInput) - 1, options)
else:
    print("Ongeldige input, programma word afgesloten")

if correct:
    print("U heeft het spel gewonnen!")
else:
    print("U heeft het foute antwoord")
