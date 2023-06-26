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
prev_guess = ""
cur_guess = ""
word = ""
reading = "False"  # Variable to understand if system is in active or passive state

while True:
    success, img = feed.read()
    img = detector.find_hands(img)
    lm_list = detector.find_position(img, draw=False)
    # print(lm_list)

    if len(lm_list) != 0:
        reading = "True"
        time.sleep(2.0)
        # print(prev_guess, cur_guess, word)
        fingers = []  # Order: Thumb, index, middle, ring, pinky
        if lm_list[tips[0]][1] > lm_list[tips[0] - 1][1]:  # For thumb. Code is for right hand. For left hand its the opposite.
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):  # For other 4 fingers
            if lm_list[tips[id]][2] < lm_list[tips[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # print(fingers)

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][2] < lm_list[6][2] and lm_list[4][2] < lm_list[10][2] and lm_list[4][2] < lm_list[14][2] and lm_list[4][2] < lm_list[18][2]:
            cur_guess = "A"

        if fingers == [0, 1, 1, 1, 1]:
            cur_guess = "B"

        if fingers == [1, 1, 1, 1, 1] and lm_list[17][1] < lm_list[18][1] < lm_list[19][1] < lm_list[20][1]:
            cur_guess = "C"

        if fingers == [0, 1, 0, 0, 0] and lm_list[4][1] < lm_list[12][1] and lm_list[4][2] > lm_list[12][2]:
            cur_guess = "D"

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][1] < lm_list[12][1] and lm_list[20][2] < lm_list[4][2]:
            cur_guess = "E"

        if fingers == [0, 0, 1, 1, 1]:
            cur_guess = "F"

        if lm_list[4][2] < lm_list[12][2] < lm_list[16][2] < lm_list[20][2] and lm_list[4][1] < lm_list[8][1] and lm_list[12][1] < lm_list[17][1] and lm_list[16][1] < lm_list[17][1] and lm_list[20][1] < lm_list[17][1]:
            cur_guess = "G"

        if lm_list[4][2] < lm_list[12][2] < lm_list[16][2] < lm_list[20][2] and lm_list[4][1] < lm_list[8][1] and lm_list[8][1] < lm_list[12][1]:
            cur_guess = "H"

        if fingers == [0, 0, 0, 0, 1] and lm_list[4][2] > lm_list[20][2]:
            cur_guess = "I"

        if fingers == [0, 0, 0, 0, 1] and lm_list[4][2] < lm_list[20][2]:
            cur_guess = "J"

        if fingers == [1, 1, 1, 0, 0] and lm_list[10][1] < lm_list[4][1] < lm_list[6][1]:
            cur_guess = "K"

        if fingers == [1, 1, 0, 0, 0]:
            cur_guess = "L"

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][2] > lm_list[6][2] and lm_list[4][2] > lm_list[10][2] and lm_list[4][2] > lm_list[14][2] and lm_list[4][2] < lm_list[19][2] and lm_list[4][1] < lm_list[10][1]:
            cur_guess = "M"

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][2] > lm_list[6][2] and lm_list[4][2] > lm_list[10][2] and lm_list[4][2] < lm_list[14][2] and lm_list[4][2] < lm_list[19][2]:
            cur_guess = "N"

        if fingers == [1, 0, 0, 0, 0] and lm_list[17][1] < lm_list[18][1] < lm_list[19][1] < lm_list[20][1] and (lm_list[8][2] - lm_list[4][2]) < 20 and lm_list[20][2] < lm_list[4][2]:
            cur_guess = "O"

        if fingers == [1, 0, 0, 0, 0] and lm_list[8][2] < lm_list[10][2] and lm_list[8][2] < lm_list[14][2] and lm_list[8][2] < lm_list[19][2] and lm_list[20][1] < lm_list[6][1]:
            cur_guess = "P"

        if fingers == [1, 0, 1, 1, 1] and lm_list[4][2] > lm_list[10][2] and lm_list[8][2] > lm_list[10][2]:
            cur_guess = "Q"

        if fingers == [0, 1, 1, 0, 0] and lm_list[8][1] < lm_list[12][2]:
            cur_guess = "R"

        if fingers == [0, 0, 0, 0, 0] and lm_list[10][2] < lm_list[4][2] < lm_list[12][2] and lm_list[6][2] < lm_list[4][2] < lm_list[8][2] and lm_list[4][1] > lm_list[10][1]:
            cur_guess = "S"

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][2] > lm_list[6][2] and lm_list[4][2] < lm_list[10][2] and lm_list[4][2] < lm_list[14][2] and lm_list[4][2] < lm_list[19][2]:
            cur_guess = "T"

        if fingers == [0, 1, 1, 0, 0] and (lm_list[8][1] - lm_list[12][1]) < 20:
            cur_guess = "U"

        if fingers == [0, 1, 1, 0, 0] and (lm_list[8][1] - lm_list[12][1]) > 20:
            cur_guess = "V"

        if fingers == [0, 1, 1, 1, 0]:
            cur_guess = "W"

        if fingers == [0, 1, 0, 0, 0] and lm_list[10][2] < lm_list[4][2] < lm_list[12][2]:
            cur_guess = "X"

        if fingers == [1, 0, 0, 0, 1] and lm_list[20][1] < lm_list[4][1] and lm_list[17][1] < lm_list[13][1]:
            cur_guess = "Y"

        if cur_guess != prev_guess:
            word = word + cur_guess
            cv2.putText(img, f'Letter: {cur_guess}', (50, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            # print(cur_guess)
            prev_guess = cur_guess
            # time.sleep(2.0)

    if len(lm_list) == 0 and reading == "True":
        print(word)
        prev_guess = ""
        cur_guess = ""
        word = ""
        reading = "False"

    cur_time = time.time()
    fps = 1 / (cur_time - prev_time)
    prev_time = cur_time

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)



