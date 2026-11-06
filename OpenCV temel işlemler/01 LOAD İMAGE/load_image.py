# !pip install opencv_python

import cv2 as cv

path = 'OpenCV temel işlemler/'

img = cv.imread('picture.png')
cv.imshow('özet penceresim', img)
cv.waitKey(0)
cv.destroyAllWindows()

dst = cv.applyColorMap(img, cv.COLORMAP_AUTUMN)
cv.imshow('dst', dst)
cv.waitKey(0)


dst = cv.applyColorMap(img, cv.COLORMAP_WINTER)
cv.imshow('dst', dst)
cv.waitKey(0)

dst = cv.applyColorMap(img, cv.COLORMAP_SPRING)
cv.imshow('dst', dst)
cv.waitKey(0)

dst = cv.applyColorMap(img, cv.COLORMAP_TWILIGHT)
cv.imshow('dst', dst)
cv.waitKey(0)

dst = cv.applyColorMap(img, cv.COLORMAP_SUMMER)
cv.imshow('dst', dst)
cv.waitKey(0)
