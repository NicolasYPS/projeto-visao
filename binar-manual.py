import numpy as np
from PIL import Image
import os

def nearest_neighbor_resize(image, new_height, new_width):
    """
    Redimensiona uma imagem usando o algoritmo Nearest Neighbor.
    
    Args:
        image: Matriz numpy representando a imagem (H x W x C)
        new_height: Nova altura da imagem
        new_width: Nova largura da imagem
    
    Returns:
        Matriz numpy da imagem redimensionada
    """
    # Obtém dimensões da imagem original
    height, width = image.shape[:2]
    
    # Cria uma matriz vazia para a nova imagem
    resized = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)
    
    # Calcula a proporção entre as imagens
    y_ratio = height / new_height
    x_ratio = width / new_width
    
    # Preenche a nova imagem
    for y in range(new_height):
        for x in range(new_width):
            # Encontra a posição correspondente na imagem original
            src_y = int(y * y_ratio)
            src_x = int(x * x_ratio)
            
            # Garante que não exceda os limites
            src_y = min(src_y, height - 1)
            src_x = min(src_x, width - 1)
            
            # Copia o valor do pixel
            resized[y, x] = image[src_y, src_x]
    
    return resized

def main():
    # Obter o diretório atual do script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Caminhos completos para as imagens
    img_road_path = os.path.join(current_dir, 'imagens', 'img_road.jpg')
    superman_path = os.path.join(current_dir, 'imagens', 'superman.jpeg')
    
    # Verificar se os arquivos existem
    if not os.path.exists(img_road_path):
        print(f"Erro: Arquivo não encontrado: {img_road_path}")
        print(f"Conteúdo do diretório 'imagens': {os.listdir(os.path.join(current_dir, 'imagens'))}")
        return
    
    if not os.path.exists(superman_path):
        print(f"Erro: Arquivo não encontrado: {superman_path}")
        print(f"Conteúdo do diretório 'imagens': {os.listdir(os.path.join(current_dir, 'imagens'))}")
        return
    
    # Carrega as imagens com PIL (biblioteca mais leve)
    img_road = np.array(Image.open(img_road_path))
    superman = np.array(Image.open(superman_path))
    
    # Define o novo tamanho (300x300 pixels)
    new_size = (300, 300)
    
    # Redimensiona as imagens manualmente
    road_resized = nearest_neighbor_resize(img_road, new_size[0], new_size[1])
    superman_resized = nearest_neighbor_resize(superman, new_size[0], new_size[1])
    
    # Converte para tons de cinza (manualmente)
    def to_grayscale(image):
        return np.dot(image[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
    
    road_gray = to_grayscale(road_resized)
    superman_gray = to_grayscale(superman_resized)
    
    # Binarização manual - CORRIGIDO: garantir que o resultado seja uint8
    def binarize(image, threshold=128):
        # Criar uma cópia para não modificar a imagem original
        result = np.zeros_like(image, dtype=np.uint8)
        # Definir pixels acima do limiar como 255 (branco)
        result[image > threshold] = 255
        return result
    
    road_binary = binarize(road_gray, 200)
    superman_binary = binarize(superman_gray, 145)
    
    # Combina as imagens para exibição
    def combine_images():
        # Converte cinza para RGB para poder combinar
        def gray_to_rgb(image):
            # Garantir que a imagem está em uint8
            if image.dtype != np.uint8:
                image = image.astype(np.uint8)
            return np.stack([image] * 3, axis=-1)
        
        # Verificar se as imagens binárias estão no formato correto
        if road_binary.dtype != np.uint8:
            road_binary_corrected = road_binary.astype(np.uint8)
        else:
            road_binary_corrected = road_binary
            
        if superman_binary.dtype != np.uint8:
            superman_binary_corrected = superman_binary.astype(np.uint8)
        else:
            superman_binary_corrected = superman_binary
        
        # Monta a grade 2x3
        col1 = np.vstack([
            road_resized.astype(np.uint8), 
            gray_to_rgb(road_gray), 
            gray_to_rgb(road_binary_corrected)
        ])
        
        col2 = np.vstack([
            superman_resized.astype(np.uint8), 
            gray_to_rgb(superman_gray), 
            gray_to_rgb(superman_binary_corrected)
        ])
        
        return np.hstack([col1, col2])
    
    # Cria e salva a imagem combinada
    combined = combine_images()
    
    # Garantir que o array combinado está no formato correto
    if combined.dtype != np.uint8:
        combined = combined.astype(np.uint8)
    
    # Salvar a imagem
    Image.fromarray(combined).save('resultado-manual.jpg')
    
    # Mostra a imagem (opcional)
    Image.fromarray(combined).show()
    
    print("Processamento concluído! Resultado salvo em 'resultado-manual.jpg'")

if __name__ == "__main__":
    main()