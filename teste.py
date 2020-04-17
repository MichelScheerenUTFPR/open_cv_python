import cv2.cv2 as cv2


cv2.namedWindow('image')
video = cv2.VideoCapture(0)
while True:
    #ret, img = video.read()
    img = cv2.flip(video.read()[1], 1)
    cv2.imshow("image", img)
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()