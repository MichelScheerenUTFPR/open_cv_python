import cv2.cv2 as cv2


def draw_rectangle(event, x, y, flags, param):  # mouse callback function
    global x_inicial, y_inicial, x_final, y_final, drawing, media
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
        if abs(x_inicial - x_final) > 2 and abs(y_inicial - y_final) > 2:
            garantirNaoInversaoDesenho()
            calcularMedia()


def garantirNaoInversaoDesenho():
    global x_inicial, x_final, y_inicial, y_final
    x1, y1 = min(x_inicial, x_final), min(y_inicial, y_final)
    x2, y2 = x1 + abs(x_inicial - x_final), y1 + abs(y_inicial - y_final)
    x_inicial, x_final, y_inicial, y_final = x1, x2, y1, y2


def calcularMedia():
    global img, y_inicial, y_final, x_inicial, x_final
    try:
        print(img[y_inicial + 1:y_final - 1, x_inicial + 1:x_final - 1].mean(axis=0).mean(axis=0))
    except RuntimeWarning as erro:
        print('Região Inválida! Erro: {}'.format((erro.__class__)))


def desenharRetangulo():
    global img, x_inicial, y_inicial, x_final, y_final
    if x_inicial != -1 and x_final != -1:
        cv2.rectangle(img, (x_inicial, y_inicial), (x_final, y_final), (0, 0, 255), 1)


drawing = False  # Verdadeiro quando o mouse está apertado, False caso contrário
x_inicial, y_inicial, x_final, y_final = -1, -1, -1, -1
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)
video = cv2.VideoCapture(0)
video.set(3, 640)  # definir largura para 640 (padrão é 640X480)
video.set(4, 480)  # definir altura para 480 (padrão é 640X480)
video.set(5, 60)  # tenta aumentar o fps, se possível
while True:
    #ret, img = video.read()
    img = cv2.flip(video.read()[1], 1)
    desenharRetangulo()
    cv2.imshow("image", img)
    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
