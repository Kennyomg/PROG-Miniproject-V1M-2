def randomhint():
    import random
    hints = ['hint1','hint2', 'hint3']
    print(random.choice(hints))
punten = 25

while True:
    if punten >= 1:
        vraag = input("Druk 'a', 'b', 'c' of 'd' voor uw antwoord")
        if vraag == 'd':
            print('U hebt de vraag goed beantwoord en u hebt ' + str(punten) + ' scoren verdient.')
            break
        elif vraag == 'hint' or vraag == 'Hint':
            punten = punten - 3
            randomhint()
        else:
            punten=punten-1
            print('Uw antwoord is helaas fout en uw score is '+str(punten-25))
            print('Doe het opnieuw:')


while True:
    nieuweVraag = input("Wilt u andere vragen beantwoorden?\n Druk 'y' voor ja en 'n' voor nee \n")
    if nieuweVraag=='n':
        print('U hebt :' +str(punten)+' score.')
        break
    elif nieuweVraag=='y':
        vraag = input("Druk 'a', 'b', 'c' of 'd' voor uw antwoord")
        if vraag == 'c':
            print('U hebt de vraag goed beantwoord en u hebt ' + str(punten) + ' score verdient')
            print('Uw totale scoren zijn: ' + str(punten*2))
            break
        elif vraag == 'hint' or vraag == 'Hint':
            punten = punten - 3
            randomhint()
        else:
            punten = punten - 1
            print('Uw antwoord is helaas fout en u hebt nu: '+str(punten)+' score.')

    else:
        print("INVALID INPUT!!! Druk alleen op 'y' of 'n' voor uw antwoord")