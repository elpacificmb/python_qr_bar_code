import time
import cv2  # opencv-python module to Read image/video/camera input
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3 - Width
cap.set(4, 480)  # 4 - Height
used_codes = []
verified_codes = []

camera = True
while camera:
    success, frame = cap.read()

    for code in decode(frame):
        code_data = code.data.decode('utf-8')

        if code_data not in verified_codes:
            print('Approved. You can Enter')
            print(code.type)
            print(code_data)
            verified_codes.append(code_data)
            # time.sleep(5)
        else:
            print('Denied. Code already used')
            # time.sleep(5)

        if code_data in verified_codes:
            result = 'Authorized'
            color = (0, 255, 0)
            print(result, color)
        else:
            result = 'Un-Authorized'
            color = (0, 0, 255)
            print(result, color)

        points = np.array([code.polygon], np.int32)
        points = points.reshape((-1, 1, 2))
        cv2.polylines(frame, [points], True, color, 5)
        points2 = code.rect
        cv2.putText(frame, result, (points2[0], points2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow('code-scan', frame)
    cv2.waitKey(1)
