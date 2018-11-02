# import numpy as np
import cv2
# from matplotlib import pyplot as plt
cap = cv2.VideoCapture('qwe.flv')
# print(mask)
ind = 0
changed = False
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # hist = cv2.calcHist([gray], [0], mask, [256], [0, 256])
    # print(len(hist))
    video = gray[0:int(720 / 8)]
    tt = []
    for i in video:
        tt.append(i[0:int(1280 / 20)])
    val = 0
    for i in tt:
        for o in i:
            val += o[2]
    x = val / ((720 / 8) * (1280 / 20))
    if x < 15 and not changed:
        print(x, ind)
        changed = True
    elif x > 15 and changed:
        print(x, ind)
        changed = False
    # gray = cv2.cvtColor(frame, cv2.COLOR_)

    # cv2.imshow('frame', frame)
    # print(gray)
    # break
    ind += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()