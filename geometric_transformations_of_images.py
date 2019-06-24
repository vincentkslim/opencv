import numpy as np
import cv2 as cv

img = cv.imread('data/messi5.jpg')
# cv.imshow('original', img)


# res = cv.resize(img,None,fx=2, fy=2, interpolation=cv.INTER_LINEAR)
# cv.imshow('scaled', res)

rows, cols = img.shape[:2]

def rotate():
    for i in range(0, 500):
        # M = np.float32([[1,0,0],
        #                 [0,1,i]])
        M = cv.getRotationMatrix2D((cols//2, rows//2), i, 0.5)
        res = cv.warpAffine(img, M, (cols, rows))
        cv.imshow('image', res)
        cv.waitKey(10)

def affine_transformation():
    # pts1 = np.float32([[10,10],[20,20],[30,30]])
    # pts2 = np.float32([[10,100],[20,200],[30, 300]])
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
    M = cv.getAffineTransform(pts1, pts2)
    res = cv.warpAffine(img, M, (cols, rows))
    cv.imshow('image', res)
    cv.waitKey(0)

def perspective_transoformation():
    global rows, cols
    img = cv.imread('data/sudoku.png', cv.IMREAD_UNCHANGED)
    pts1 = np.float32([[75, 87], [491, 71], [37, 514], [519, 519]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

    M = cv.getPerspectiveTransform(pts1, pts2)

    res = cv.warpPerspective(img, M, (300, 300))
    cv.imshow('original', img)
    cv.imshow('image', res)
    cv.waitKey(0)

perspective_transoformation()
cv.destroyAllWindows()
