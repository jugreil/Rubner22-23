import random
import requests
from prettytable import PrettyTable
import cv2
import mediapipe as mp
import msvcrt
import json

username = ""
usedSymbols = {}
dicSchere = {"Stein" : 0,"Papier":1,"Schere":2,"Spock":3,"Echse":4}

def menu():
    while True:
        print("1. Play")
        print("2. See Personal Data")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            play()
        elif choice == "2":
            see_personal_data()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

def play():
    while True:
        print("1. Normal")
        print("2. Hard")
        print("3. Gesturecontrolled")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            play_normal_mode(False)
        elif choice == "2":
            play_normal_mode(True)
        elif choice == "3":
            play_with_gesture_Control()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

def send_data_from_User(symbol, count):
    url = "http://localhost:5000/submit"
    data = {"Name": username, "Symbol": symbol, "Count": count}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Successfully sent data to Server")
    else:
        print("Failed to send JSON to API. Error code: ", response.status_code)

def see_personal_data():
    data = get_player_data(username)
    if "data" in data:
        table = PrettyTable()
        table.field_names = ["Symbol", "Count"]
        for i in data["data"]:
            table.add_row([i["Symbol"], i["Count"]])
        print(table)
    else:
        print(data["error"])

def play_normal_mode(hardcore):
    while(True):
        print("Bitte wählen Sie ihr zerstörerisches Element oder Exit um auszusteigen")
        print("Schere, Stein, Papier, Spock, Echse")
        inputYouser = input("Jetzt Eingeben: ")
        if inputYouser == "Exit":
            for i in usedSymbols:
                send_data_from_User(i,usedSymbols[i])
            break
        if not hardcore:
            inputCoumputer = random.choice(list(dicSchere))
        else:
            data = get_player_data(username)
            count = 0
            mostUsedSymbol = ""
            if "data" in data:
                for i in data["data"]:
                    if count < i["Count"]:
                        count = i["Count"]
                        mostUsedSymbol = i["Symbol"]
            inputCoumputer = mostUsedSymbol
            for i in usedSymbols:
                send_data_from_User(i,usedSymbols[i])
                usedSymbols = {}
        print("The Computer chose " + inputCoumputer)
        if youWon(inputYouser, inputCoumputer) == 1:
            print("You won against a Computer")
        elif youWon(inputYouser, inputCoumputer) == -1:
            print("You lost against a computer")
        elif youWon(inputYouser, inputCoumputer) == 0:
            print("You achieved a draw against a computer")
        else:
            print("There happened something unexpected")
def youWon(keyYouser, keyComputer):
    def addSymbolToDic(symbol):
        if symbol in usedSymbols:
            usedSymbols[symbol] += 1
        else:
            usedSymbols[symbol] = 1
    if not keyYouser in dicSchere:
        return
    addSymbolToDic(keyYouser)
    if keyYouser == keyComputer:
        return 0
    youserValue = dicSchere[keyYouser]
    computerValue = dicSchere[keyComputer]

    for i in range(1,3):
        if(youserValue + 2*i)%5 == computerValue:
            return 1
    return -1
def get_player_data(name):
    url = f"http://localhost:5000/player/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        player_data = response.json()
        return player_data
    else:
        return {"error" : response.json()}


def play_with_gesture_Control():
    dataToCompare = None
    url = "http://localhost:5000/gesture"
    response = requests.get(url)
    if response.status_code == 200:
        dataToCompare = response.json()
        print("Loaded data successfully from server")
    else:
        print("Failed to send JSON to API. Error code: ", response.status_code)
        return
    consistenceCheck = []
    print("please make sure your hand faces the camera straight")
    print("in the best case your laptop screen has a 90° angle to the desk")
    print("When you press the esc button you will leave the gesture controlled game")
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    def getDeltaToPoint(arrayOfAllPoints):
        referencePoint = arrayOfAllPoints[0]
        arrayOfAllPoints.pop(0)
        deltaArray = []
        for point in arrayOfAllPoints:
            newPointx = abs(point[0] - referencePoint[0])
            newPointy = abs(point[1] - referencePoint[1])
            deltaArray.append([newPointx,newPointy,point[2]])
        return deltaArray

    def compareData(arrayOfAllPoints, pointsForComparison):
        overlapingPointsCounter = []
        counter = 0
        for points in pointsForComparison:
            for i in range(20):
                for r in range(3):
                    counter += abs(pointsForComparison[points][i][r] - arrayOfAllPoints[i][r])
            overlapingPointsCounter.append([points,counter])
            counter = 0
        
        choice = ""
        value = 10000
        for i in range(5):
            if value > overlapingPointsCounter[i][1]:
                value = overlapingPointsCounter[i][1]
                choice = overlapingPointsCounter[i][0]
        return choice
    
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if cv2.waitKey(5) & 0xFF == 27:
                    cap.release()
                    cv2.destroyAllWindows()
                    return
            if cv2.waitKey(33) == ord('a'):
                if len(consistenceCheck) == 10:
                    if len(set(consistenceCheck)) == 1:
                        print("you chose the symbol: " + consistenceCheck[0])
                        inputCoumputer = random.choice(list(dicSchere))
                        print("The computer chose the symbo: " + inputCoumputer)
                        if youWon(consistenceCheck[0], inputCoumputer) == 1:
                            print("You won against a Computer")
                        elif youWon(consistenceCheck[0], inputCoumputer) == -1:
                            print("You lost against a computer")
                        elif youWon(consistenceCheck[0], inputCoumputer) == 0:
                            print("You achieved a draw against a computer")
                        else:
                            print("There happened something unexpected")
                    else:
                        print("please try again there wasn't an consistent enough gesture recognized")
                else:
                    print("There wasn't enough time to get enough data")
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    allMarksInList = []
                    normalizedLandmark = hand_landmarks.landmark
                    if len(normalizedLandmark) == 21:  
                        for mark in normalizedLandmark:
                            allMarksInList.append([mark.x,mark.y,mark.z])
                        consistenceCheck.append(compareData(getDeltaToPoint(allMarksInList),dataToCompare).lstrip("Result"))
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())
            image = cv2.flip(image, 1)
            if len(consistenceCheck) > 10:
                consistenceCheck.pop(0)
                cv2.putText(image, consistenceCheck[-1], (75,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
            cv2.imshow('MediaPipe Hands', image )
    cap.release()




if __name__ == "__main__":
    if username == "":
        username = input("Please enter your username: ")
        print(f"Welcome, {username}!")
    menu()
    

