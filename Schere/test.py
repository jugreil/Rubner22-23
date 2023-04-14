import cv2
import mediapipe as mp
import msvcrt
import json

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
allDeltas = []
start = False
count = 0
def getDeltaToPoint(arrayOfAllPoints):
    referencePoint = arrayOfAllPoints[0]
    arrayOfAllPoints.pop(0)
    deltaArray = []
    for point in arrayOfAllPoints:
        newPointx = abs(point[0] - referencePoint[0])
        newPointy = abs(point[1] - referencePoint[1])
        deltaArray.append([newPointx,newPointy,point[2]])
    return deltaArray

def compareData(arrayOfAllPoints):
    overlapingPointsCounter = 0
    pointsForComparison = []
    with open("schereResult.json", "r") as file:
        pointsForComparison = json.load(file)
    for i in range(20):
        for r in range(3):
            if pointsForComparison[i][r]-0.05 <= arrayOfAllPoints[i][r] <= pointsForComparison[i][r] + 0.05:
                overlapingPointsCounter += 1
    print(overlapingPointsCounter)

# For webcam input:
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
        if results.multi_hand_landmarks:
            allMarksInList = []
            normalizedLandmark = results.multi_hand_landmarks[0].landmark
            if len(normalizedLandmark) == 21:  
                for mark in normalizedLandmark:
                    allMarksInList.append([mark.x,mark.y,mark.z])
            if cv2.waitKey(5) & 0xFF == 27:
                print("start")
                start = True
            if start and count < 1000:
                allDeltas.append(getDeltaToPoint(allMarksInList))
                count += 1
            if start and count >= 1000:
                break
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
cap.release()

with open("stein.json", "w") as file:
    json.dump(allDeltas, file)