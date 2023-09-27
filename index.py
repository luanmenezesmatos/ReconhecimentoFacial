import cv2  # Importar o OpenCV para manipular imagens
import datetime  # Importar o módulo "datetime" para pegar o timestamp atual
import numpy as np  # Importar o NumPy para manipular matrizes
import os  # Importar o módulo "os" para manipular arquivos
import time  # Importar o módulo "time" para manipular o tempo

# Importando o arquivo do banco de dados
from src.structures.Database import Database
# Importando o arquivo de reconhecimento facial
from src.structures.FaceRecognition import FaceRecognition

# Instanciando a classe do banco de dados
database = Database(host="localhost", user="root",
                    password="", database="db_recfacial")

timestamp = str(datetime.datetime.now().timestamp()).replace(".", "")

# Criando a função para perguntar se a pessoa deseja usar o reconhecimento facial pela câmera (webcam) ou pela imagem


def check():
    # Pergunta
    pergunta = input("Olá! Seja bem-vindo(a) ao sistema de reconhecimento facial! Selecione as opções abaixo:\n\n1 - Reconhecimento facial pela câmera (Webcam)\n2 - Reconhecimento facial pela imagem\n3 - Cadastrar uma pessoa\n4- Fazer o reconhecimento facial\n\nDigite a opção desejada: ")

    # Verificar se a opção digitada é válida
    match pergunta:
        case "1":
            # Reconhecimento facial pela câmera (webcam)

            # Instanciando a classe de reconhecimento facial
            faceRecognition = FaceRecognition()

            name = input("Digite o nome da pessoa: ")
            print(f"Olá, {name}! Vamos tirar uma foto sua!")

            faces = faceRecognition.detectFace(name, timestamp)
            if faces:
                for face in faces:
                    if face:
                        # Pegar a imagem para salvar no banco de dados
                        image = cv2.imread(
                            f"assets/faces/{name}-{timestamp}.jpg")
                        image_path = f"assets/faces/{name}-{timestamp}.jpg"

                        print("Salvando no banco de dados...")

                        def getImageFromFile(image):
                            res = np.fromfile(image, dtype=np.uint8)
                            print(res)
                            return cv2.imdecode(res, cv2.IMREAD_UNCHANGED)

                        get_image = getImageFromFile(image_path)

                        def getBytesFromImage(image):
                            return cv2.imencode('.jpg', image)[1].tobytes()

                        get_bytes = getBytesFromImage(get_image)

                        # Deletar a imagem do diretório "assets/faces"
                        print("Deletando a imagem do diretório...")
                        # Esperar 5 segundos para deletar a imagem
                        time.sleep(5)
                        os.remove(image_path)
                        print("Imagem deletada com sucesso!")

                        database.insert(name, get_bytes)

                        print("Foto cadastrada com sucesso!")
                if cv2.waitKey(5) == 27:
                    return None
                cv2.destroyAllWindows()
            else:
                print(
                    "Não foi possível tirar a foto, pois não detectamos nenhum rosto. Tente novamente.")
        case "2":
            # Reconhecimento facial pela imagem

            # Instanciando a classe de reconhecimento facial
            faceRecognition = FaceRecognition()

            # Perguntar o nome da pessoa
            name = input("Digite o nome da pessoa: ")

            # Verificar se o nome informado é um caminho de uma imagem (usar o os), caso for, mostrar uma mensagem de erro
            if os.path.exists(name) or name.endswith(".jpg") or name.endswith(".jpeg"):
                print("O nome informado é um caminho de uma imagem. Tente novamente.")
                return None

            # Perguntar o caminho da imagem
            image_path = input(
                "Digite o caminho da imagem que deseja fazer o reconhecimento facial: ")
            
            # Verificar a extensão da imagem
            if image_path.endswith(".jpeg"):
                # Converter para .jpg
                image_path = image_path.replace(".jpeg", ".jpg")

            # Verificar se o caminho da imagem existe
            if os.path.exists(image_path):
                # Fazer o reconhecimento facial
                face = faceRecognition.recognizeFace(image_path)
                if face:
                    # Se o rosto for detectado, mostrar o nome da pessoa
                    print(f"Olá, {name}! Seu rosto foi detectado!")

                    # Pegar a imagem para salvar no banco de dados
                    image = cv2.imread(image_path)

                    print("Salvando no banco de dados...")

                    def getImageFromFile(image):
                        res = np.fromfile(image, dtype=np.uint8)
                        print(res)
                        return cv2.imdecode(res, cv2.IMREAD_UNCHANGED)

                    get_image = getImageFromFile(image_path)

                    def getBytesFromImage(image):
                        return cv2.imencode('.jpg', image)[1].tobytes()

                    get_bytes = getBytesFromImage(get_image)

                    database.insert(name, get_bytes)

                    print("Foto cadastrada com sucesso!")

                    # Deletar a imagem do diretório "assets/faces"
                    print("Deletando a imagem do diretório...")

                    # Esperar 5 segundos para deletar a imagem
                    time.sleep(5)

                    os.remove(image_path)

                    print("Imagem deletada com sucesso!")
                else:
                    # Se o rosto não for detectado, mostrar uma mensagem de erro
                    print("Não foi possível detectar o seu rosto. Tente novamente.")
            else:
                # Se o caminho da imagem não existir, mostrar uma mensagem de erro
                print("O caminho da imagem não existe. Tente novamente.")

            #
        case "3":
            # Cadastrar uma pessoa

            # Perguntar o nome da pessoa
            name = input("Digite o nome da pessoa: ")

            # Verificar se o nome informado é um caminho de uma imagem (usar o os), caso for, mostrar uma mensagem de erro
            if os.path.exists(name) or name.endswith(".jpg") or name.endswith(".jpeg"):
                print("O nome informado é um caminho de uma imagem. Tente novamente.")
                return None

            # Perguntar o caminho da imagem
            image_path = input(
                "Digite o caminho da imagem que deseja cadastrar: ")
            
            # Verificar a extensão da imagem
            if image_path.endswith(".jpeg"):
                # Converter para .jpg
                image_path = image_path.replace(".jpeg", ".jpg")

            # Verificar se o caminho da imagem existe
            if os.path.exists(image_path):
                # Fazer o reconhecimento facial
                face = faceRecognition.recognizeFace(image_path)
                if face:
                    # Se o rosto for detectado, mostrar o nome da pessoa
                    print(f"Olá! O rosto de {name} foi detectado!")

                    # Pegar a imagem para salvar no banco de dados
                    image = cv2.imread(image_path)

                    print("Salvando no banco de dados...")

                    def getImageFromFile(image):
                        res = np.fromfile(image, dtype=np.uint8)
                        print(res)
                        return cv2.imdecode(res, cv2.IMREAD_UNCHANGED)

                    get_image = getImageFromFile(image_path)

                    def getBytesFromImage(image):
                        return cv2.imencode('.jpg', image)[1].tobytes()

                    get_bytes = getBytesFromImage(get_image)

                    database.insert(name, get_bytes)

                    print("Foto cadastrada com sucesso!")

                    # Deletar a imagem do diretório "assets/faces"
                    print("Deletando a imagem do diretório...")

                    # Esperar 5 segundos para deletar a imagem
                    time.sleep(5)

                    os.remove(image_path)

                    print("Imagem deletada com sucesso!")
                else:
                    # Se o rosto não for detectado, mostrar uma mensagem de erro
                    print("Não foi possível detectar o seu rosto. Tente novamente.")
            else:
                # Se o caminho da imagem não existir, mostrar uma mensagem de erro
                print("O caminho da imagem não existe. Tente novamente.")
        case 4:
            # Fazer o reconhecimento facial (pela câmera ou pela imagem) no banco de dados

            # Perguntar o nome da pessoa
            name = input("Digite o nome da pessoa: ")

            # Verificar se o nome informado é um caminho de uma imagem (usar o os), caso for, mostrar uma mensagem de erro
            if os.path.exists(name) or name.endswith(".jpg") or name.endswith(".jpeg"):
                print("O nome informado é um caminho de uma imagem. Tente novamente.")
                return None
            
            # Verificar se o nome informado existe no banco de dados


            
        case _:
            # Opção inválida
            print("\n\nOpção inválida. Tente novamente.")


# Chamando a função "check" para iniciar o programa
check()
