import cv2 as cv
import numpy as np

def show_image(image, title='image'):
    cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

img_original = cv.imread(r'data/opencv-logo.png')
show_image(img_original)
img = cv.cvtColor(img_original, cv.COLOR_BGR2HSV)

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

mask1 = cv.inRange(img, lower_red, upper_red)
show_image(mask1, 'red1')

lower_red = np.array([170, 100, 100])
upper_red = np.array([180, 255, 255])

mask2 = cv.inRange(img, lower_red, upper_red)
show_image(mask2, 'red2')

mask = cv.bitwise_or(mask1, mask2)
show_image(mask, 'red all')

lower_green = np.array([50, 100, 100])
upper_green = np.array([70, 255, 255])

mask1 = cv.inRange(img, lower_green, upper_green)
show_image(mask1, 'green')

mask = cv.bitwise_or(mask, mask1)
show_image(mask, 'green+red')

lower_blue = np.array([110, 100, 100])
upper_blue = np.array([130, 255, 255])

mask1 = cv.inRange(img, lower_blue, upper_blue)
show_image(mask1, 'blue')

mask = cv.bitwise_or(mask, mask1)
show_image(mask, 'green+red+blue')

res = cv.bitwise_and(img_original, img_original, mask=mask)
show_image(res, 'result')