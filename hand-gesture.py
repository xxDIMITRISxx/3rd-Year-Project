import cv2
import numpy as np
import serial
import time
from random import choice
from tensorflow.keras.models import load_model

#training data 2
# REV_CLASS_MAP = {
#     0: "0 - empty",
#     1: "1 - index",
#     2: "2 - peace",
#     3: "3 - three fingers",
#     4: "4 - rock",
#     5: "5 - palm",
#     6: "6 - spiderman",
#     7: "7 - call me"
# }
#training data 1
REV_CLASS_MAP = {
    0: "0 - empty",
    1: "1 - index",
    2: "2 - peace",
    3: "3 - spiderman",
    4: "4 - rock",
    5: "5 - palm"
}
# COM PORT is the port 3
# baud rate set to 9600
# number of data
# arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
#
# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.5)
#     data = arduino.readline()
#     return data

def mapper(value):
    return REV_CLASS_MAP[value]

def main():
    img_shape = (225, 225)
    #training data 1
    model = load_model("hand-gesture-model1.h5")
    #training data 2
    #model = load_model("hand-gesture-model2.h5")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video")

    counter = 0
    temp = None
    # if its True, then the inputs value go for the joints
    #other wise the inputs value go for the angle of the joint
    jointOrAngle = True
    numberString = ""
    numberInt = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # rectangle for input sub-frame
        cv2.rectangle(frame, (75, 75), (300, 300), (0, 0, 255), 2)

        # extract the region of image within the input sub-frame
        capture_region = frame[75:300, 75:300]
        img = cv2.cvtColor(capture_region, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, img_shape)

        # predict the move made
        pred = model.predict(np.array([img]))
        move_code = mapper(np.argmax(pred[0]))

        # display the move made
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Your Move: " + move_code, (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

        numberString = move_code[0]
        numberInt = int(numberString)

        # ----- Arduino code ----- #
        # if jointOrAngle:
        #     if temp == move_code:
        #         counter += 1
        #     else:
        #         temp = move_code
        #         counter = 0
        #     print(counter)
        #
        #     if counter == 30:
        #         print("Gesture : " + move_code + " passed!")
        #         # gesture detected => send the number
        #         if numberInt in range(1, 6):
        #             write_read(numberString)
        #             if numberInt != 5:
        #                 jointOrAngle = False
        #         counter = 0
        #
        # if jointOrAngle == False:
        #     if counter > 180:
        #         counter = 0
        #     if numberInt == 5:
        #         counter += 1
        #     print(counter)
        #     if numberInt == 4:
        #         counter = round(counter)
        #         counterString = str(counter)
        #         write_read((counterString))
        #         counter = 0
        #         jointOrAngle = True

        # ----- ----------- ------ #

        cv2.imshow("Hand Gesture Recognition - press q to exit", frame)

        k = cv2.waitKey(10)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()