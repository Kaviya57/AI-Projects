import cv2

import imutils

img = cv2.imread('Flower1.png')

resizedImg = imutils.resize(img, width=50)

cv2.imwrite('Flower2.jpg', resizedImg)
