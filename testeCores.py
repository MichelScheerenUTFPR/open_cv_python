import cv2


img = cv2.imread("imagem.png")
# r = cv2.selectROI(img, False)
cv2.rectangle(img, (330, 30), (360, 50), (0, 0, 255), 1)
cv2.imshow("image", img)
img2 = img[31:49, 331:359]
"img2 = img[y1+1:y2-1, x1+1:x2-1]"
print(img2.mean(axis=0).mean(axis=0))

while True:
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
