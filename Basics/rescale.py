import cv2 as cv


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# For Image Resize
img = cv.imread('../Resources/Photos/cat.jpg')
rescale_img = rescale_frame(img)
cv.imshow('image', img)
cv.imshow('Resized Image', rescale_img)

cv.waitKey(0)

# For video Resize
cap = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = cap.read()

    if isTrue:
        resized_frame = rescale_frame(frame, scale=.2)
        cv.imshow('Frame', frame)
        cv.imshow('Resized Frame', resized_frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
