# Processamento de Imagens Manualmente (sem OpenCV) 

Um projeto simples para demonstrar técnicas básicas de processamento de imagens sem depender de bibliotecas especializadas, implementando manualmente operações como redimensionamento, conversão para tons de cinza e binarização. 

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green?logo=opencv)](https://opencv.org/)
[![Pillow](https://img.shields.io/badge/Pillow-10.0%2B-orange?logo=python)](https://python-pillow.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-red?logo=numpy)](https://numpy.org/)
   
    
# Visão Geral 

Este projeto implementa técnicas fundamentais de processamento de imagens manualmente, sem usar bibliotecas como OpenCV. O foco está em: 

    Entender a lógica por trás das operações de visão computacional
    Reduzir a carga computacional mantendo detalhes críticos
    Demonstrar como bibliotecas como OpenCV funcionam internamente
     

Projeto proposto pelo Bootcamp bairesdev machine learning training e DIO. 

## Pré-requisitos 

Antes de executar o projeto, certifique-se de ter: 

    Python 3.8 ou superior
    pip (geralmente vem com o Python)
    Pillow e NumPy (para processamento manual)
    OpenCV e NumPy (para comparação com biblioteca)
     

## Como usar e configurar ambiente virtual 

1. Criar ambiente virtual 

```bash 
python3 -m venv venv
``` 
 
2. Ativar ambiente (Linux/Mac) 
```bash
source venv/bin/activate
 ```
 
3. Ativar ambiente (Windows) 
```bash
venv\Scripts\activate
``` 
 
4. Instalar dependências 
```bash
pip install -r requirements.txt
```  
 
## Executar o código 

- Processamento via biblioteca (OpenCV) 


    ```bash
    python binar-cv.py
    ``` 
 
- Processamento manual (sem biblioteca especializada) 


    ```bash
    python binar-manual.py
    ```
 
## Resultados 

O programa exibe uma janela única com 6 imagens organizadas em 2 colunas e 3 linhas: 

- Coluna 1: Processamento da imagem da estrada
- Coluna 2: Processamento da imagem do Superman
- Linhas: Imagem original, em tons de cinza e binarizada
     

<img src="imagens/resultado.png" alt="Exemplo de saída" width="600" />

### Explicação Técnica 

**Redimensionamento (implementação manual)** 

 ```bash
def nearest_neighbor_resize(image, new_height, new_width):
    height, width = image.shape[:2]
    resized = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)
    y_ratio = height / new_height
    x_ratio = width / new_width
    
    for y in range(new_height):
        for x in range(new_width):
            src_y = int(y * y_ratio)
            src_x = int(x * x_ratio)
            src_y = min(src_y, height - 1)
            src_x = min(src_x, width - 1)
            resized[y, x] = image[src_y, src_x]
    
    return resized
 ```
 

Reduz a resolução da imagem para um tamanho padrão (300x300 pixels)
Usa algoritmo Nearest Neighbor para preservar detalhes importantes
Reduz significativamente a carga computacional
     

**Conversão para Tons de Cinza (implementação manual)** 

```bash
def to_grayscale(image):
    return np.dot(image[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
 
 ```

Converte de 3 canais (RGB) para 1 canal
Usa fórmula padrão: Y = 0.299R + 0.587G + 0.114*B
Reduz os dados em 66% sem perder informações visuais críticas
     

**Binarização (implementação manual)** 

```bash
def binarize(image, threshold=128):
    result = np.zeros_like(image, dtype=np.uint8)
    result[image > threshold] = 255
    return result
 ```
 

Aplica limiar para converter em preto e branco
Mantém contornos essenciais para reconhecimento
Facilita detecção de objetos e padrões
     

## Aplicações Práticas 

Esta técnica é usada em: 

- Sistemas de visão para veículos autônomos
- Reconhecimento de objetos em tempo real
- Processamento de documentos
- Análise de imagens médicas
     

## Como Contribuir 

Contribuições são bem-vindas! Siga estes passos: 

    Faça um fork do repositório
    Crie uma branch para sua feature (git checkout -b feature/nova-feature)
    Commit suas mudanças (git commit -am 'Adiciona nova feature')
    Faça push para a branch (git push origin feature/nova-feature)
    Abra um Pull Request
     

Autor 

Nicolas Souza

LinkedIn  | GitHub  