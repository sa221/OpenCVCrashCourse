import cv2 as cv

# Read an image
# img = cv.imread('../Resources/Photos/cat_large.jpg')
#
# cv.imshow('Image', img)
#
# cv.waitKey(0)

# Read Videos

cap = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = cap.read()
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()

