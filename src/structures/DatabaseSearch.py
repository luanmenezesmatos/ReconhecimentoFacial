# Buscar a imagem do rosto da pessoa no banco de dados

# Importar o arquivo do banco de dados para fazer a conexão
from src.structures.Database import Database

# Importar o módulo "cv2" para manipular imagens
import cv2

# Importar o módulo "os" para manipular arquivos
import os

# Importar o módulo "time" para fazer uma pausa
import time

# Importar o módulo "mediapipe" para detecção de rostos
import mediapipe as mp

class DatabaseSearch:
    def __init__(self):
        # Instanciar a classe do banco de dados
        self.database = Database(host="localhost", user="root", password="", database="db_recfacial")

    def compare(self, image1, image2):
        # Instanciar o módulo de detecção de rostos
        faceDetection = mp.solutions.face_detection

        # Instanciar o detector de rostos
        faceDetector = faceDetection.FaceDetection()

        # Ler as imagens
        image1 = cv2.imread(image1)
        image2 = cv2.imread(image2)

        # Detectar os rostos nas imagens
        faces1 = faceDetector.process(image1)
        faces2 = faceDetector.process(image2)

        # Se algum rosto for detectado, retornar "True" (verdadeiro) caso contrário, retornar "False" (falso)
        if faces1.detections and faces2.detections:
            return True
        else:
            return False
    
    # A função "search" irá receber a foto do rosto da pessoa e irá buscar no banco de dados por uma imagem igual ou parecida
    def search(self, name, face):
        # Fazer a busca no banco de dados por um rosto cujo o seu nome é igual ao nome do usuário
        results = self.database.select(name)

        # Se não houver nenhum resultado, retornar "False"
        if not results:
            return False

        # Converter o resultado da busca no banco de dados (que é uma imagem no formato BLOB) para um arquivo de imagem
        with open(f"assets/temp/{name}.png", "wb") as file:
            file.write(results)

        # compare = self.compare(cv2.imread(face), cv2.imread(f"assets/temp/{name}.png"))

        #compare = self.compare(cv2.imread(f"assets/images/{face}"), cv2.imread(f"assets/temp/{name}.png"))

        face_path = os.path.join(os.getcwd(), "assets", "images", face)
        name_path = os.path.join(os.getcwd(), "assets", "temp", f"{name}.png")

        compare = self.compare(face_path, name_path)

        if compare == True:
            print("Deletando a imagem temporária...")
            time.sleep(5) # Fazer uma pausa de 5 segundos
            os.remove(f"assets/temp/{name}.png") # Deletar a imagem temporária

            return True
        else:
            os.remove(f"assets/temp/{name}.png") # Deletar a imagem temporária

            return False