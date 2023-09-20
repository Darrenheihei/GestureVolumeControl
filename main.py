import cv2
import HandTrackingModule as htm

def main():
    cap = cv2.VideoCapture(1)
    detector = htm.HandDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        img, lmList = detector.findPositions(img, handID=[0], lmID_draw=[4, 8], drawSize=10)

        maxDist = 380 # the maximum pixel distance of the two fingers of my hand
        minDist = 35 # the mimimum pixel distance of the two fingers of my hand
        if lmList: # that means we detected the hand
            # print(pow((lmList[4].x - lmList[8].x)**2 + (lmList[4].y - lmList[8].y)**2, 1/2))
            volume = int((pow((lmList[4].x - lmList[8].x)**2 + (lmList[4].y - lmList[8].y)**2, 1/2) - minDist)/(maxDist - minDist) * 100)
            volume = min(volume, 100)
            volume = max(volume, 0)

            # draw the volume control bar
            length = 300
            if volume < 10:
                cv2.putText(img, str(volume), (55, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            elif volume < 100:
                cv2.putText(img, str(volume), (45, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            else: # volume = 100
                cv2.putText(img, str(volume), (35, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.rectangle(img, (30, 150 + length), (100, 150 + length - int(volume/100 * length)), (0, 255, 0), cv2.FILLED)
            cv2.rectangle(img, (30, 150 + length), (100, 150), (255, 0, 0), 3)

        cv2.imshow("Gesture Volume Control", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return

if __name__ == "__main__":
    main()