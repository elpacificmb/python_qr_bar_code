import cv2  # opencv module to Read image/video/camera input
from pyzbar.pyzbar import decode

img = cv2.imread('myqrcode.png')

for code in decode(img):
    print(code.type)
    print(code.data.decode('utf-8'))
