import random
import json

list = []
dictionary = {}

def Create_List():
    for i in range(1, 46):
        list.append(i)

def Create_Dictionary():
    keys = range(1, 46)
    for i in keys:
        dictionary[i] = 0

def Lottoziehung():
    zufallszahlen = []
    lotto = list[:]
    for i in range(5):
        zufall = random.choice(lotto)
        lotto.remove(zufall)
        zufallszahlen.append(zufall)
    return zufallszahlen

def Stats(count):
    for i in range(count):
        for j in Lottoziehung():
            dictionary[j] += 1
    print(json.dumps(dictionary, indent=2)) # pretty print

Create_List()
Create_Dictionary()
Stats(1000)
