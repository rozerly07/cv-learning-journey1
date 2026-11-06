# !pip install opencv_python

import cv2 as cv

path = 'OpenCV temel işlemler/'

img = cv.imread('picture.png')
cv.namedWindow('colored_img', cv.WINDOW_AUTOSIZE)
cv.imshow('colored_img', img)
cv.waitKey(0)

# cvt gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.waitKey(0)

# imwrite
cv.imwrite('picture_gray.png', gray)
cv.destroyAllWindows()

img = cv.imread('picture.png' , cv.IMREAD_GRAYSCALE)
cv.namedWindow('colored_img', cv.WINDOW_AUTOSIZE)
cv.imshow('colored_img', img)
cv.waitKey(0)


