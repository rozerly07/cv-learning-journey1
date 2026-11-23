import cv2
import cv2 as cv
import numpy as np

path = 'OpenCV temel işlemler/'

#resim1 birinci ve ikinci index verilen değere göre sarı rengi elde ederiz
# sıfırıncı index yazılmadığı için 0 değerini alır
src1 = np.zeros(shape = (400, 400, 3), dtype =np.uint8)
src1[100:200, 100:200, 1] = 255
src1[100:200, 100:200, 2] = 255
cv2.imshow('input2', src1)
cv2.waitKey(0)

#resim2
src2 = np.zeros(shape = (400, 400, 3), dtype =np.uint8)
src2[100:200, 100:200, 1] = 255
cv2.imshow('input2', src2)
cv2.waitKey(0)

#RGB
#BGR (pyhton da, yani yukarıdaki degerler asağıdaki indexlere göredir)

# 0: B (1. index)
# 1: G
# 2: R

# and
dst1 = cv.bitwise_and(src1, src2)
cv2.imshow('dst1', dst1)
cv2.waitKey(0)

# or: iki pixelden biri sıfırdan büyükse true
dst2 = cv.bitwise_and(dst1, dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)


dst3 = cv.bitwise_and(dst1, dst1)
cv2.imshow('dst3', dst3)
cv2.waitKey(0)
