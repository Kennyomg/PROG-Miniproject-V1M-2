import time
import hashlib
import json
import random

def MarvelCharacters():
    #Maken van de API Url

    timestamp = time.time()
    publicApiKey = 'ce72ea27bb97e27dbf4b8be2decb44ee'
    privateApiKey = 'dfaa8dfee51de0c124a3ee2b4bd8e6d15ba1b4fa'
    stringToHash = str(timestamp) + privateApiKey + publicApiKey
    hash_object = hashlib.md5(stringToHash.encode())
    md5Hash = hash_object.hexdigest()
    apiUrl = 'http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}'.format(timestamp, publicApiKey, md5Hash)
    #print(apiUrl)   # deze moet op gegeven moment uit de code weggehaald worden
    # voorbeeld voor hoe het eruit komt te zien en deze kun je dan in Visual Studio Code gebruiken
    # http://gateway.marvel.com/v1/public/characters?ts=1539531767.861436&apikey=ce72ea27bb97e27dbf4b8be2decb44ee&hash=1efc26ce5b2905641dd9413bfe6662d8


    # Aanroepen van API Url

    import requests #pip install requests uitvoeren in Terminal om te installeren voor de 1e keer
    response = requests.get(apiUrl)

    # Resultaten van API in Json omzetten naar dictionary
    apiResults = json.loads(response.text)

    # Alle characters uitlezen uit API
    allCharacters = apiResults['data']['results']

    return  allCharacters


def giveHint(chosenchar):
    #chooseCharacter(MarvelCharacters())
    description = str(chosenchar["description"])

    description.replace(chosenchar["character"], "___")

    print(description)

    return "tekst"

'''
# start programma
print('quiz gestart')
name = input('Wat is je naam: ')
allCharacters = MarvelCharacters() #Finish
chosenCharacter = chooseCharacter(allCharacters)#nog open #LET OP: Er mag geen Character gekozen worden met een lege discription, daar kunnen we geen hints vandaan halen

hint = giveHint(chosenCharacter)# nog open
# hints eerst uit discription halen van de gekozen character
'''
def chooseCharacter(apilst):
    allCharacters = apilst #read api list
    charlst = [] #create fresh list for char names
    descriplst = [] #create fresh list for descriptions

    for character in allCharacters:
        charlst.append(character['name']) #add char to char list
        descriplst.append(character['description']) #add descrip to descrip list

    randomselect = random.choice(charlst) #select random char

    while True:
        descriptionchar = descriplst[charlst.index(randomselect)]
        if len(descriptionchar) >= 1: #if descrip of selected char >1 let prog know
            print('{}'.format(randomselect))
            break
        else:                                                 #if descrip of selected char non exist let prog know
            randomselect = random.choice(charlst)

    return {'character':randomselect,'description':descriptionchar} #return character and descrip for later use


giveHint(chooseCharacter(MarvelCharacters()))
