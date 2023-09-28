# Buscar a imagem do rosto da pessoa no banco de dados

# Importar o arquivo do banco de dados para fazer a conexão
from src.structures.Database import Database

# Importar o módulo "cv2" para manipular imagens
import cv2

# Importar o módulo "os" para manipular arquivos
import os

# Importar o módulo "time" para fazer uma pausa
import time

class DatabaseSearch:
    def __init__(self):
        # Instanciar a classe do banco de dados
        self.database = Database(host="localhost", user="root", password="", database="db_recfacial")

    # Criando a função de comparação de imagens usando o algoritmo "ORB"
    def compare(self, face1, face2):
        # Fazer a comparação das imagens usando algoritmos de visão computacional do OpenCV
        # O algoritmo "ORB" é um algoritmo de visão computacional que compara imagens

        # Instanciar o algoritmo "ORB"
        orb = cv2.ORB_create()

        # Extrair as características da imagem do rosto da pessoa
        kp1, des1 = orb.detectAndCompute(face1)

        # Extrair as características da imagem do rosto da pessoa
        kp2, des2 = orb.detectAndCompute(face2)

        # Instanciar o algoritmo "BFMatcher"
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Fazer a comparação das características das imagens
        matches = bf.match(des1, des2)

        # Ordenar as características das imagens
        matches = sorted(matches, key=lambda x: x.distance)

        print(len(matches))

        # Se a quantidade de características for maior que 20, retornar "True"
        if len(matches) > 20:
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

        compare = self.compare(cv2.imread(f"assets/images/{face}"), cv2.imread(f"assets/temp/{name}.png"))
        """ face_path = os.path.join(os.getcwd(), "assets", "images", face)
        name_path = os.path.join(os.getcwd(), "assets", "temp", f"{name}.png")

        compare = self.compare(face_path, name_path) """

        if compare == True:
            print("Deletando a imagem temporária...")
            time.sleep(5) # Fazer uma pausa de 5 segundos
            os.remove(f"assets/temp/{name}.png") # Deletar a imagem temporária

            return True
        else:
            os.remove(f"assets/temp/{name}.png") # Deletar a imagem temporária

            return False