import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def harris_detection():

    image = cv.imread("cat_image.jpg")

    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    gray_img = np.float32(gray_img)

    corners_img = cv.cornerHarris(gray_img,3 ,3, 0.04)

    image[corners_img>0.001*corners_img.max()] = [255, 0, 0]

    plt.figure()
    plt.subplot(131)
    plt.title('Harris Detection')
    plt.imshow(image)
    plt.axis('off')

    plt.show()

def shi_tomasi():
    image = cv.imread("sudoku.jpg")

    gray_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    corners_img = cv.goodFeaturesToTrack(gray_img, 1000, 0.01, 10)

    corners_img = np.intp(corners_img)

    for corners in corners_img:
        x,y = corners.ravel()
        cv.circle(image, (x, y), 3, [255,0,0], -1)

    plt.figure()
    plt.subplot(132)
    plt.title("Shi Tomasi")
    plt.imshow(image)
    plt.axis('off')

    plt.show()

def canny_edge_detection():
    image = cv.imread("cat_image.jpg")

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    blurred = cv.GaussianBlur(gray_image, (5, 5), 40)

    edges = cv.Canny(blurred, threshold1=140, threshold2=170)

    plt.figure()
    plt.subplot(133)
    plt.title("Canny Edge Detection")
    plt.imshow(edges)
    plt.show()


harris_detection()
shi_tomasi()
canny_edge_detection()
