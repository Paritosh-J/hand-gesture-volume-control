'''
    Detect hands using cv2 & mediapipe library
    Draw lines to connect the landmarks of the detected hands
'''
import cv2
import mediapipe as mp

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectConfidence=0.75, trackConfidence=0.75):
        self.mode = mode
        self.maxHands = maxHands
        self.detectConfidence = detectConfidence
        self.trackConfidence = trackConfidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands() # process a RGB image & return the hand landmarks of detected hands
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, frame, draw=True):
        # convert img from BGR to RGB for hands object to process
        rgbImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(rgbImg)
        if self.result.multi_hand_landmarks:
            for handLmarks in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, handLmarks, self.mpHands.HAND_CONNECTIONS) # draw landmarks & connections for them
        return frame

    def findPosition(self, frame, handNo=0, draw=True):
        LmarkList = []
        rgbImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(rgbImg)
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo] # processed landmarks from Hands() method for 1 hand
            # get land mark ids
            for LmarkId, lmk in enumerate(myHand.landmark):
                h, w, c = frame.shape  # get o/p window dimension
                # coordinates for landmakrs of detected hands
                cx, cy = int(lmk.x * w), int(lmk.y * h)
                print(LmarkId, cx, cy)  # print id & coord. of landmarks on console
                LmarkList.append([LmarkId, cx, cy])

                if draw:
                    if LmarkId == 4:  # id of thumb tip
                        cv2.circle(frame, (cx, cy), 15, (84, 245, 66), cv2.FILLED)  # draw circle for thumb tip

                    if LmarkId == 8:  # id of index finger tip
                        cv2.circle(frame, (cx, cy), 15, (84, 245, 66), cv2.FILLED)  # draw circle for thumb tip

                    if LmarkId == 12:  # id of middle finger tip
                        cv2.circle(frame, (cx, cy), 15, (84, 245, 66), cv2.FILLED)  # draw circle for thumb tip

                    if LmarkId == 16:  # id of ring finger tip
                        cv2.circle(frame, (cx, cy), 15, (84, 245, 66), cv2.FILLED)  # draw circle for thumb tip

                    if LmarkId == 20:  # id of pinky tip
                        cv2.circle(frame, (cx, cy), 15, (84, 245, 66), cv2.FILLED)  # draw circle for thumb tip
        return LmarkList


def main():
    video = cv2.VideoCapture(0)  # open camera to capture image frame
    detect = handDetector()
    # make o/p window of free dimension
    cv2.namedWindow('=== Live Cam ===', cv2.WINDOW_NORMAL)

    while True:
        check, frame = video.read()  # check & capture the frame
        frame = cv2.flip(frame, 1) # flip the frame for a mirror image like o/p
        frame = detect.findHands(frame)
        LmarkList = detect.findPosition(frame) # get hand landmarks and store in a list

        cv2.putText(frame, "Press 'Q' to exit", (25, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)  # display quit key on o/p window
        cv2.imshow('=== Live Cam ===', frame) # open window for showing the o/p

        # escape key (q)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == "__main__":
    main()
