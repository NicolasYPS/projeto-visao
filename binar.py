import cv2
import numpy as np

def resize_image(image, target_size=(300, 300)):
    """Redimensiona a imagem para um tamanho padrão."""
    return cv2.resize(image, target_size)

# Carrega e redimensiona as imagens
img1 = resize_image(cv2.imread('imagens/img_road.jpg'))
img2 = resize_image(cv2.imread('imagens/superman.jpeg'))

if img1 is None or img2 is None:
    print("Erro: Uma ou ambas as imagens não foram encontradas.")
    exit()

# Processamento da primeira imagem (img_road.jpg)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
_, binary1 = cv2.threshold(gray1, 200, 255, cv2.THRESH_BINARY)

# Processamento da segunda imagem (superman.jpeg)
# O valor do limiar foi ajustado para 145 para melhor visualização
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, binary2 = cv2.threshold(gray2, 145, 255, cv2.THRESH_BINARY)

# Combina as imagens em uma grade 2x3 (2 colunas, 3 linhas)
column1 = np.vstack([
    img1,
    cv2.cvtColor(gray1, cv2.COLOR_GRAY2BGR),
    cv2.cvtColor(binary1, cv2.COLOR_GRAY2BGR)
])

column2 = np.vstack([
    img2,
    cv2.cvtColor(gray2, cv2.COLOR_GRAY2BGR),
    cv2.cvtColor(binary2, cv2.COLOR_GRAY2BGR)
])

# Combina as duas colunas horizontalmente
combined = np.hstack([column1, column2])

# Exibe todas as imagens em uma única janela
cv2.imshow("Processamento de Imagens", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()