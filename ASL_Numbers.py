import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm


wCam, hCam = 640, 480
prev_time = 0

feed = cv2.VideoCapture(0)
feed.set(3, wCam)
feed.set(4, hCam)

detector = htm.HandDetector(detection_confidence=0.75)
tips = [4, 8, 12, 16, 20]

while True:
    success, img = feed.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)
    # print(lm_list)

    if len(lm_list) != 0:
        fingers = []
        if lm_list[tips[0]][1] > lm_list[tips[0] - 1][1]:  # For thumb. Code is for right hand. For left hand its the opposite.
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):  # For other 4 fingers
            if lm_list[tips[id]][2] < lm_list[tips[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        print(fingers)

        if fingers == [1, 0, 0, 0, 0] and lm_list[17][1] < lm_list[18][1] < lm_list[19][1] < lm_list[20][1] and (lm_list[8][2] - lm_list[4][2]) < 20:
            cv2.putText(img, f'Count: 0', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [0, 1, 0, 0, 0]:
            cv2.putText(img, f'Count: 1', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [0, 1, 1, 0, 0]:
            cv2.putText(img, f'Count: 2', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [1, 1, 1, 0, 0]:
            cv2.putText(img, f'Count: 3', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [0, 1, 1, 1, 1]:
            cv2.putText(img, f'Count: 4', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [1, 1, 1, 1, 1]:
            cv2.putText(img, f'Count: 5', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [0, 1, 1, 1, 0]:
            cv2.putText(img, f'Count: 6', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [0, 1, 1, 0, 1]:
            cv2.putText(img, f'Count: 7', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [0, 1, 0, 1, 1]:
            cv2.putText(img, f'Count: 8', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        if fingers == [0, 0, 1, 1, 1]:
            cv2.putText(img, f'Count: 9', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)



    cur_time = time.time()
    fps = 1 / (cur_time - prev_time)
    prev_time = cur_time

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

