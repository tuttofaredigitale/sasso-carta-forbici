import random
import re
while (1 < 2):
    print ("\n")
    print ("Sasso, carta, forbici - Scegli!")
    userChoice = input("Scegli la tua arma [S]asso, [C]arta, o [F]orbici: ")
    if not re.match("[FfSsCc]", userChoice):
        print ("Per favore, scegli una lettera:")
        print ("[S]asso, [C]arta, o [F]orbici.")
        continue
    print ("La tua scelta: " + userChoice)
    choices = ['S', 'C', 'F']
    opponenetChoice = random.choice(choices)
    print ("Io ho scelto: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print ("Parità! ")
    #if opponenetChoice == str("R") and str.upper(userChoice) == "P"
    elif opponenetChoice == 'S' and userChoice.upper() == 'F':      
        print ("Sasso batte forbici, Ho vinto! ")
        continue
    elif opponenetChoice == 'F' and userChoice.upper() == 'C':      
        print ("Le forbici battono la carta! Ho vinto! ")
        continue
    elif opponenetChoice == 'C' and userChoice.upper() == 'S':      
        print ("Carta batte sasso, Ho vinto! ")
        continue
    else:       
        print ("Hai vinto!")
