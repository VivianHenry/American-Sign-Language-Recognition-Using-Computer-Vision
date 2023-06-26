import cv2
import mediapipe as mp
import time


class HandDetector:
    def __init__(self, mode=False, max_hands=2, model_complexity = 1, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.model_complexity = model_complexity
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mpHands = mp.solutions.hands  # Instance of class hands
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.model_complexity, self.detection_confidence, self.track_confidence)
        self.mpDraw = mp.solutions.drawing_utils  # Drawing utilities for connecting the tracking points

    def find_hands(self, img, draw=True):
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Needs to be in RGB form for hand class
        self.results = self.hands.process(img_RGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:  # Get info for each hands' landmark in feed
                if draw:
                    self.mpDraw.draw_landmarks(img, hand_lms, self.mpHands.HAND_CONNECTIONS)

        return img

    def find_position(self, img, hand_no = 0, draw = True):
        lm_list = []

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):  # Gives the ID and position (in image ratio) of all the landmarks
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
                if draw:
                    if id == 0:  # Tracking the base of the palm
                        cv2.circle(img, (cx, cy), 15, (92, 49, 6), cv2.FILLED)

        return lm_list


'''Dummy code to test this module'''


def main():
    feed = cv2.VideoCapture(0)  # Starts the webcam
    prev_time, cur_time = 0, 0

    detector = HandDetector()

    while True:
        success, img = feed.read()
        img = detector.find_hands(img)
        lm_list = detector.find_position(img)
        if len(lm_list) != 0:
            print(lm_list[4])  # Pick which landmark to see

        cur_time = time.time()
        fps = 1 / (cur_time - prev_time)
        prev_time = cur_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 0), 3)

        cv2.imshow("Live Feed", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
