import poker
import cv2
import adb_tool as atool

while True:
    img = atool.getScreenshot()
    img = cv2.resize(img, (int(img.shape[1] * 0.4), int(img.shape[0] * 0.4)), interpolation=cv2.INTER_CUBIC)

    print(poker.get_my_pokers(img))
    print(poker.get_others_pokers(img))

