# This is a sample Python script.
import random
import time


# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Kombinationen:
    royal_flush = 0
    straight_flush = 0
    vierling = 0
    full_house = 0
    flush = 0
    straße = 0
    drilling = 0
    zwei_paare = 0
    ein_paar = 0
    hohe_karte = 0


calculated_percentage = [50.1, 42.3, 4.75, 2.11, 0.392, 0.197, 0.144, 0.0240, 0.0014, 0.000154]
kombinationen = Kombinationen()


def kartenAnalysieren(arr):
    arr_zahlen = []
    arr_farben = []
    for i in arr:
        arr_zahlen.append(i % 13)
    for i in arr:
        arr_farben.append(i // 13)
    heufigste_zahl = max(arr_zahlen, key=arr_zahlen.count)
    anzahl_heufigst_zahl = arr_zahlen.count(heufigste_zahl)
    match anzahl_heufigst_zahl:
        case 1:
            arr_zahlen.sort()
            if 5 == arr_farben.count(arr_farben[0]):
                if arr_zahlen[4] - 4 == arr_zahlen[0]:
                    if arr_zahlen[4] == 12:
                        kombinationen.royal_flush += 1
                        return
                    kombinationen.straight_flush += 1
                    return
                kombinationen.flush += 1
            elif arr_zahlen[4] - 4 == arr_zahlen[0]:
                kombinationen.straße += 1
            else:
                kombinationen.hohe_karte += 1
            return
        case 2:
            arr_zahlen.remove(heufigste_zahl)
            heufigste_zahl = max(arr_zahlen, key=arr_zahlen.count)
            anzahl_heufigst_zahl = arr_zahlen.count(heufigste_zahl)
            if anzahl_heufigst_zahl == 2:
                kombinationen.zwei_paare += 1
            else:
                kombinationen.ein_paar += 1
            return
        case 3:
            for i in range(3):
                arr_zahlen.remove(heufigste_zahl)
            heufigste_zahl = max(arr_zahlen, key=arr_zahlen.count)
            anzahl_heufigst_zahl = arr_zahlen.count(heufigste_zahl)
            if anzahl_heufigst_zahl == 2:
                kombinationen.full_house += 1
                return
            kombinationen.drilling += 1
            return
        case 4:
            kombinationen.vierling += 1
            return


def pokerDeckErstellen():
    arr = [i for i in range(52)]
    return arr


def kartenZiehen(arr):
    random.shuffle(arr)
    return arr[-5:]


def kartenZiehenSelberMachen(arr):
    for i in range(5):
        rand = random.randint(0, 51 - i)
        arr[rand], arr[51 - i] = arr[51 - i], arr[rand]
    return arr[-5:]


if __name__ == '__main__':
    durchleufe = 20000000
    pokerDeck = pokerDeckErstellen()
    for i in range(durchleufe):
        kartenAnalysieren(kartenZiehenSelberMachen(pokerDeck))
    print(vars(kombinationen))
    zaehler = 0
    for key in sorted(vars(kombinationen), key=vars(kombinationen).get, reverse=True):
        print("{0}: {1} -> {2}% -> {3}% (calculated) ".format(key, vars(kombinationen)[key],
                                                              round(vars(kombinationen)[key] / durchleufe * 100, 5),
                                                              calculated_percentage[zaehler]))
        zaehler += 1
    """
    startTime = time.time_ns()
    for i in range(100000):
        kartenZiehen(pokerDeck)
    firstTime = time.time_ns()
    for i in range(100000):
        kartenAnalysieren(kartenZiehenSelberMachen(pokerDeck))
    secoundTime = time.time_ns()
    print("Python library in nanosekunden:")
    print(firstTime - startTime)
    print("selber gemacht in nanosekunden:")
    print(secoundTime-firstTime)
    print("Unterschied der Methoden in sekunden")
    print(((firstTime - startTime)-(secoundTime-firstTime))/1000000000)
    print("Unterschied in prozent:")
    print((firstTime - startTime)/(secoundTime-firstTime))
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
