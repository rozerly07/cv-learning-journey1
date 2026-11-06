import cv2 as cv
import numpy as np

src1 = cv.imread('me.jpg')
src2 = cv.imread('meow.jpg')

h, w, ch = src1.shape
src2 = cv.resize(src2, (w, h))
print("h, w, ch:", h, w, ch)

#add
add_result = np.zeros(src1.shape, src2.dtype)
cv.add(src1, src2, add_result)
cv.imshow('add_result', add_result)
cv.waitKey(0)
cv.destroyAllWindows()

#substract
subresult = np.zeros(src1.shape, src2.dtype)
cv.subtract(src1, src2, subresult)
cv.imshow('subresult', subresult)
cv.waitKey(0)
cv.destroyAllWindows()

#multiplay
mul_result = np.zeros(src1.shape, src2.dtype)
cv.multiply(src1, src2, mul_result)
cv.imshow('mul_result' , mul_result)
cv.waitKey(0)
cv.destroyAllWindows()

#divine
div_result = np.zeros(src1.shape, src2.dtype)
cv.divide(src1, src2, div_result)
cv.imshow('divresult', div_result)
cv.waitKey(0)
cv.destroyAllWindows()
