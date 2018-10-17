punten = 25

while True:
    if punten >= 1: #The player should have at least one point to start the test.
        character = input("Kies het goede antwoord:\n 'a', 'b', 'c' 'd' ") # The player must select the good answer from: A,B,C,D.
        if character == 'd': #This is the correct answer (pretend).
            print('U hebt de vraag goed beantwoord en u hebt ' + str(punten) + ' scoren verdient.')

        else:
            punten = punten - 1 #If the answer is not correct, the player losses one point.
            print('Uw antwoord is helaas fout en uw score is ' + str(punten - 25))
            print('Doe het opnieuw:') # The player can not go to the next question.

        while True:
            character = input("Kies het goede antwoord\n 'a', 'b', 'c' of 'd' ") #If the first answer was correct, player can answer this question.
            if character == 'c':
                print('U hebt de vraag goed beantwoord en u hebt ' + str(punten) + ' score verdient')
                print('Uw totale scoren zijn: ' + str(punten * 2))
                break

            else:
                punten = punten - 1 # The player losses one point by clicking on wrong answer.
                print('Uw antwoord is helaas fout en u hebt nu: ' + str(punten) + ' score.')

