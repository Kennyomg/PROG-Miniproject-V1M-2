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
    print(apiUrl)   # deze moet op gegeven moment uit de code weggehaald worden
    # voorbeeld voor hoe het eruit komt te zien en deze kun je dan in Visual Studio Code gebruiken
    # http://gateway.marvel.com/v1/public/characters?ts=1539531767.861436&apikey=ce72ea27bb97e27dbf4b8be2decb44ee&hash=1efc26ce5b2905641dd9413bfe6662d8


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
gekozenCharacter = kiesCharacter(allCharacters)#nog open #LET OP: Er mag geen Character gekozen worden met een lege discription, daar kunnen we geen hints vandaan halen

hint = geefHint(gekozenCharacter)# nog open
# hints eerst uit discription halen van de gekozen character


