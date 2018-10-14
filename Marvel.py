import time
import hashlib
import json

def alleCharacters():
    #Maken van de API Url

    timestamp = time.time()
    publicApiKey = 'ce72ea27bb97e27dbf4b8be2decb44ee'
    privateApiKey = 'dfaa8dfee51de0c124a3ee2b4bd8e6d15ba1b4fa'
    stringToHash = str(timestamp) + privateApiKey + publicApiKey
    hash_object = hashlib.md5(stringToHash.encode())
    md5Hash = hash_object.hexdigest()
    apiUrl = 'http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}'.format(timestamp, publicApiKey, md5Hash)

    # Aanroepen van API Url

    import requests #pip install requests uitvoeren in Terminal om te installeren voor de 1e keer
    response = requests.get(apiUrl)

    # Resultaten van API in Json omzetten naar dictionary
    apiResultaten = json.loads(response.text)

    # Alle characters uitlezen uit API
    allCharacters = apiResultaten['data']['results']

    return  allCharacters

def kiesCharacter(allCharacters):
    # Code aanmaken om een character random te kiezen
    return allCharacters[0]

def geefHint(gekozenCharacter):
    # Code aanmaken om hint te genereren
    return "tekst"

# start programma
print('quizgestart')
naam = input('Wat is je naam: ')
allCharacters = alleCharacters() #Finish
gekozenCharacter = kiesCharacter(allCharacters)#nog open

hint = geefHint(gekozenCharacter)# nog open


