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
        print(fingers)

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][2] < lm_list[6][2] and lm_list[4][2] < lm_list[10][2] and lm_list[4][2] < lm_list[14][2] and lm_list[4][2] < lm_list[18][2]:
            cv2.putText(img, f'Letter: A', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 1, 1, 1, 1]:
            cv2.putText(img, f'Letter: B', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [1, 1, 1, 1, 1] and lm_list[17][1] < lm_list[18][1] < lm_list[19][1] < lm_list[20][1]:
            cv2.putText(img, f'Letter: C', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 1, 0, 0, 0] and lm_list[4][1] < lm_list[12][1] and lm_list[4][2] > lm_list[12][2]:
            cv2.putText(img, f'Letter: D', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][1] < lm_list[12][1] and lm_list[20][2] < lm_list[4][2]:
            cv2.putText(img, f'Letter: E', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 0, 1, 1, 1]:
            cv2.putText(img, f'Letter: F', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if lm_list[4][2] < lm_list[12][2] < lm_list[16][2] < lm_list[20][2] and lm_list[4][1] < lm_list[8][1] and lm_list[12][1] < lm_list[17][1] and lm_list[16][1] < lm_list[17][1] and lm_list[20][1] < lm_list[17][1]:
            cv2.putText(img, f'Letter: G', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if lm_list[4][2] < lm_list[12][2] < lm_list[16][2] < lm_list[20][2] and lm_list[4][1] < lm_list[8][1] and lm_list[8][1] < lm_list[12][1]:
            cv2.putText(img, f'Letter: H', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 0, 0, 0, 1] and lm_list[4][2] > lm_list[20][2]:
            cv2.putText(img, f'Letter: I', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 0, 0, 0, 1] and lm_list[4][2] < lm_list[20][2]:
            cv2.putText(img, f'Letter: J', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [1, 1, 1, 0, 0] and lm_list[10][1] < lm_list[4][1] < lm_list[6][1]:
            cv2.putText(img, f'Letter: K', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [1, 1, 0, 0, 0]:
            cv2.putText(img, f'Letter: L', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][2] > lm_list[6][2] and lm_list[4][2] > lm_list[10][2] and lm_list[4][2] > lm_list[14][2] and lm_list[4][2] < lm_list[19][2] and lm_list[4][1] < lm_list[10][1]:
            cv2.putText(img, f'Letter: M', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][2] > lm_list[6][2] and lm_list[4][2] > lm_list[10][2] and lm_list[4][2] < lm_list[14][2] and lm_list[4][2] < lm_list[19][2]:
            cv2.putText(img, f'Letter: N', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [1, 0, 0, 0, 0] and lm_list[17][1] < lm_list[18][1] < lm_list[19][1] < lm_list[20][1] and (lm_list[8][2] - lm_list[4][2]) < 20 and lm_list[20][2] < lm_list[4][2]:
            cv2.putText(img, f'Letter: O', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [1, 0, 0, 0, 0] and lm_list[8][2] < lm_list[10][2] and lm_list[8][2] < lm_list[14][2] and lm_list[8][2] < lm_list[19][2] and lm_list[20][1] < lm_list[6][1]:
            cv2.putText(img, f'Letter: P', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [1, 0, 1, 1, 1] and lm_list[4][2] > lm_list[10][2] and lm_list[8][2] > lm_list[10][2]:
            cv2.putText(img, f'Letter: Q', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 1, 1, 0, 0] and lm_list[8][1] < lm_list[12][2]:
            cv2.putText(img, f'Letter: R', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 0, 0, 0, 0] and lm_list[10][2] < lm_list[4][2] < lm_list[12][2] and lm_list[6][2] < lm_list[4][2] < lm_list[8][2] and lm_list[4][1] > lm_list[10][1]:
            cv2.putText(img, f'Letter: S', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 0, 0, 0, 0] and lm_list[4][2] > lm_list[6][2] and lm_list[4][2] < lm_list[10][2] and lm_list[4][2] < lm_list[14][2] and lm_list[4][2] < lm_list[19][2]:
            cv2.putText(img, f'Letter: T', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 1, 1, 0, 0] and (lm_list[8][1] - lm_list[12][1]) < 20:
            cv2.putText(img, f'Letter: U', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 1, 1, 0, 0] and (lm_list[8][1] - lm_list[12][1]) > 20:
            cv2.putText(img, f'Letter: V', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 1, 1, 1, 0]:
            cv2.putText(img, f'Letter: W', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [0, 1, 0, 0, 0] and lm_list[10][2] < lm_list[4][2] < lm_list[12][2]:
            cv2.putText(img, f'Letter: X', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if fingers == [1, 0, 0, 0, 1] and lm_list[20][1] < lm_list[4][1] and lm_list[17][1] < lm_list[13][1]:
            cv2.putText(img, f'Letter: Y', (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cur_time = time.time()
    fps = 1 / (cur_time - prev_time)
    prev_time = cur_time

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

