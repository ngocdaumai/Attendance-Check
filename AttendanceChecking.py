import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,900)
cap.set(4,600)

with open('personalInfo') as f:
    myDataList = f.read().splitlines()

while True:

    success, img = cap.read()
    # img = cv2.imread('8.png')
    for barcode in decode(img):
        data = barcode.data.decode('utf-8')
        if data in myDataList:
            output = 'Can attend'
            color = (0,255,0)
        else:
            output = 'Can not attend'
            color = (0, 0, 255)
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 5)
        cv2.putText(img,output,(x+5,y-6),cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,color,2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)
