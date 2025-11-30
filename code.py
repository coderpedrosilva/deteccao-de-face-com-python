# Detecção de faces

import cv2
import matplotlib.pyplot as plt

# 1) Ler a imagem
img = cv2.imread('imagem.png')

if img is None:
    print("ERRO: não consegui ler 'imagem.png'.")
    print("Verifique se o arquivo está na MESMA pasta do code.py e se o nome está correto.")
    raise SystemExit

# 2) Dimensão da figura do matplotlib (apenas visual)
plt.rcParams['figure.figsize'] = (6, 6)

# 3) Carregar o classificador de faces
# Use o caminho padrão do OpenCV para evitar problema de path
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

if face_cascade.empty():
    print("ERRO: não consegui carregar o classificador de faces.")
    raise SystemExit

# 4) Converter para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 5) Detectar faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
)

print(f"Quantidade de faces detectadas: {len(faces)}")

# 6) Desenhar retângulos nas faces
cont = 0
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cont += 1

# 7) Salvar a imagem resultante
cv2.imwrite('resultado.png', img)
print("Imagem salva como 'aragorn.png' na mesma pasta do script.")

# 8) Mostrar a imagem na tela
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
