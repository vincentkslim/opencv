import cv2

img = cv2.imread(r'data/lena.jpg', flags=cv2.IMREAD_UNCHANGED)

print(img)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('lena_copy.png', img)
