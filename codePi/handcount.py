import cv2
import mediapipe as mp
import time
from tcpcom.tcpcom import TCPServer

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.1)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0




IP_PORT = 22000



def onStateChanged(state, msg):
    print(state)
    if state == "LISTENING":
        print ("Server:-- Listening...")
    elif state == "CONNECTED":
        print ("Server:-- Connected to", msg)
    elif state == "MESSAGE":
        print ("Server:-- Message received:", msg)
        if msg == "go":
            server.sendMessage(finalCall)
            
server = TCPServer(IP_PORT, stateChanged = onStateChanged)




while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            avgX = 0
            avgY = 0
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x *w), int(lm.y*h)
                
                avgX+=cx
                avgY+=cy
                #if id ==0:
                cv2.circle(img, (cx,cy), 7, (255,0,255), cv2.FILLED)
            avgX = (avgX / len(handLms.landmark)) * 800/640
            avgY = avgY / len(handLms.landmark) * 600/480
            print(int(avgX),int(avgY))
            
            server.sendMessage(str(int(avgX )) + "," + str(int(avgY)))
            

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        video_getter.stop()
        break

