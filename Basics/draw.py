import cv2 as cv
import numpy as np

blank_img = np.zeros((400, 600, 3), dtype='uint8')
# cv.imshow('Blank', blank_img)

# Change the color of an image
blank_img[0:200, 0:600] = 45, 91, 38
blank_img[200:400, 0:600] = 255, 255, 255

# Draw Circle
cv.circle(blank_img, (blank_img.shape[1] // 2, blank_img.shape[0] // 2), 100, (0, 0, 255), thickness=-1)
cv.imshow('PlayingWithOpenCV', blank_img)

# Draw a rectangle
# cv.rectangle(blank_img, (0, 0), (20, 400), (255, 0, 0), thickness=-1)
# cv.imshow('Rect', blank_img)

# Draw line
cv.line(blank_img, (0, 0), (200, 300), (0, 0, 0), 2)

# Write text
cv.putText(blank_img, 'Bangladesh', (0, 20), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.putText(blank_img, 'Japan', (0, 220), cv.FONT_HERSHEY_TRIPLEX, 1.0, (45, 91, 38), 2)
cv.imshow('Text', blank_img)

cv.waitKey(0)
