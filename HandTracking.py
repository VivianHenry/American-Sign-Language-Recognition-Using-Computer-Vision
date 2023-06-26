import cv2
import mediapipe as mp
import time

feed = cv2.VideoCapture(0)  # Starts the webcam

mpHands = mp.solutions.hands  # Instance of class hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils  # Drawing utilities for connecting the tracking points

prev_time, cur_time = 0, 0

while True:
    success, img = feed.read()
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Needs to be in RGB form for hand class
    results = hands.process(img_RGB)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:  # Get info for each hands' landmark in feed
            for id, lm in enumerate(hand_lms.landmark):  # Gives the ID and position (in image ratio) of all the landmarks
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)  # ID, X, and Y of all the landmarks (in pixels)
                if id == 0:  # Tracking the base of the palm
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpDraw.draw_landmarks(img, hand_lms, mpHands.HAND_CONNECTIONS)

    cur_time = time.time()
    fps = 1/(cur_time - prev_time)
    prev_time = cur_time

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 0), 3)

    cv2.imshow("Live Feed", img)
    cv2.waitKey(1)