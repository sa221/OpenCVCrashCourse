import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')

cv.imshow('Park', img)


# Translation(Shift an image to the x,y axis)
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    print(transMat)
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x->Left/-y-->UP/x-->Right/y-->Down
translated = translate(img, -100, -100)
cv.imshow('Translated', translated)


# Rotation (Rotate image clock and anti-clock wise)
def rotate(img, angel, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angel, 1.0)
    print(rotMat)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow('Roated', rotated)

# Resizing Image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[0:300, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
