import cv2 as cv
import numpy as np

def mouseRGB(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        colorsB = frame[y, x ,0]
        colorsG = frame[y, x ,1]
        colorsR = frame[y, x ,2]
        colors = frame[y,x]

        print("Red: ", colorsR)
        print("Green : ", colorsG)
        print("Blue : ", colorsB)
        print("BRG Format : ", colors)

        print("Coordinates of pixels: X: ", x, "Y: ", y)

video = cv.VideoCapture("video.mp4")

cv.namedWindow("mouseRGB")
cv.setMouseCallback("mouseRGB", mouseRGB)

while(1):
    ret, frame = video.read()
    if not ret:
        break

    cv.imshow('mouseRGB', frame)
    if cv.waitKey(1) & 0XFF == ord("q"):
        break

video.release()
cv.destroyAllWindows()
