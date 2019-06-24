import cv2
import numpy as np
import math
drawing = False
mode = 'circle'
ix, iy = -1, -1

def draw_circle(event, x, y, flag, param):
    global ix, iy, drawing, mode, img, temp_img

    color = (cv2.getTrackbarPos('B', 'image'), cv2.getTrackbarPos('G', 'image'), cv2.getTrackbarPos('R', 'image'))
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == 'circle':
                img = temp_img.copy()
                cv2.circle(img, (ix, iy), distance((ix, iy), (x, y)), color, 5, cv2.LINE_AA)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'circle':
            cv2.circle(img, (ix, iy), distance((ix, iy), (x, y)), color, 5, cv2.LINE_AA)
            temp_img = img.copy()

    elif event == cv2.EVENT_MOUSEWHEEL:
        if flag > 0:
            print('scrolling up!')
        elif flag < 0:
            print('scrolling down!')


def distance(pt1, pt2):
    return int(math.sqrt((pt1[0]-pt2[0]) ** 2 + (pt1[1]-pt2[1]) ** 2))


img = np.zeros((1024, 1024, 3), np.uint8)
img += 255
temp_img = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

def nothing(x):
    pass

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)


while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()