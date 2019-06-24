import cv2
import numpy as np

def resize(img, factor):
    height, width, channel = img.shape
    new_height = int(height * factor/100)
    new_width = int(width * factor/100)
    dim = (new_width, new_height)
    return cv2.resize(img, dim)

img1 = cv2.imread(r'data/messi5.jpg')
img2 = cv2.imread(r'data/opencv-logo.png', cv2.IMREAD_ANYCOLOR)
img2 = resize(img2, 40)


mask = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(mask, 240, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

height, width, channel = img2.shape

roi = img1[:height, :width]

img1_roi = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_mask = cv2.bitwise_and(img2, img2, mask=mask)

cv2.imshow('image', img1_roi)
cv2.imshow('image2', img2_mask)
cv2.waitKey(0)

img1[:height, :width] = cv2.add(img1_roi, img2_mask)

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()