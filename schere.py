import random
dicSchere = {"Stein" : 1,"Papier":2,"Schere":3,"Spock":4,"Echse":5}

print("Sie spielen Schere Stein Papier Spock Echse gegen den Computer")
while(True):
    print("Bitte wählen Sie ihr zerstörerisches Element oder Exit um auszusteigen")
    inputYouser = input("Jetzt Eingeben: ")
    if inputYouser == "Exit":
        break
    inputCoumputer = random.choice(list(dicSchere))
    print(inputYouser)
    print(inputCoumputer)

    def youWon(keyYouser, keyComputer):
        youserValue = dicSchere[keyYouser]
        computerValue = dicSchere[keyComputer]
        for i in range(1,4):
            if(youserValue + 2*i)%5 == computerValue:
                return True
        return False

    if youWon(inputYouser, inputCoumputer):
        print("You won against a Computer")
    else:
        print("You lost against a computer")