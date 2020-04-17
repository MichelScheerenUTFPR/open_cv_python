import cv2


def eventos_retangulo(event, x, y, flags, param):  # mouse callback function
    global x_inicial, y_inicial, x_final, y_final, drawing
    if event == cv2.EVENT_LBUTTONDOWN:  # Ocorre quando o botão esquerdo do mouse é apertado
        drawing = True
        x_inicial, y_inicial = x, y
        x_final, y_final = -1, -1
    elif event == cv2.EVENT_MOUSEMOVE:  # Ocorre quando o mouse está se movendo na área
        if drawing == True:
            x_final, y_final = x, y
    elif event == cv2.EVENT_LBUTTONUP:  # Ocorre quando o botão esquerdo do mouse é liberado
        drawing = False
        x_final, y_final = x, y
        if x_inicial - x_final != 0 and y_inicial - y_final != 0:
            garantirNaoInversaoDesenho()
            calcularMedia()


def garantirNaoInversaoDesenho():
    global x_inicial, x_final, y_inicial, y_final
    x1, y1 = min(x_inicial, x_final), min(y_inicial, y_final)
    x2, y2 = x1 + abs(x_inicial - x_final), y1 + abs(y_inicial - y_final)
    x_inicial, x_final, y_inicial, y_final = x1, x2, y1, y2


def calcularMedia():
    global img, y_inicial, y_final, x_inicial, x_final
    print(img[y_inicial + 1:y_final - 1, x_inicial + 1:x_final - 1].mean(axis=0).mean(axis=0))


def desenharRetangulo():
    global img, x_inicial, y_inicial, x_final, y_final
    if x_inicial != -1 and x_final != -1:
        copia = img.copy()
        cv2.rectangle(copia, (x_inicial, y_inicial), (x_final, y_final), (0, 0, 255), 1)
        cv2.imshow("image", copia)


drawing = False  # True quando o mouse está apertado, False caso contrário
x_inicial, y_inicial, x_final, y_final = -1, -1, -1, -1
img = cv2.imread("imagem.png")
cv2.imshow("image", img)
cv2.namedWindow('image')
cv2.setMouseCallback('image', eventos_retangulo)
while True:
    desenharRetangulo()
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
