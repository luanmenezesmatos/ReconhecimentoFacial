import cv2  # Importar o OpenCV para manipular imagens
import mediapipe as mp  # Importar o MediaPipe para detecção de rostos
import os  # Importar o módulo "os" para manipular arquivos

class FaceRecognition:
    def __init__(self):
        # Instanciar o módulo de detecção de rostos
        self.faceDetection = mp.solutions.face_detection
        self.drawing = mp.solutions.drawing_utils  # Instanciar o módulo de desenho
        # Instanciar o detector de rostos
        self.faceDetector = self.faceDetection.FaceDetection()
        print("Reconhecimento facial iniciado!")

    def detectFace(self, name, timestamp):
        print("Detectando rostos...")

        webcam = cv2.VideoCapture(0)  # Instanciar a webcam

        validacao, frame = webcam.read()  # Ler a imagem da webcam
        if not validacao:
            return None
        image = frame  # Atribuir a imagem da webcam para a variável "image"
        faces = self.faceDetector.process(
            image)  # Detectar os rostos na imagem
        if faces.detections:  # Se algum rosto for detectado
            for face in faces.detections:  # Para cada rosto detectado na imagem
                # Desenhar um retângulo em volta do rosto
                self.drawing.draw_detection(image, face)

                # Salvar a imagem na pasta assets/faces
                file_name = f"{name}-{timestamp}.jpg"
                file_path = os.path.join("assets", "faces", file_name)
                # Salvar a imagem na pasta assets/faces junto com o nome do usuário e o timestamp atual
                cv2.imwrite(file_path, image)

        # Para fechar a janela da webcam, basta apertar a tecla "ESC"
        if cv2.waitKey(5) == 27:
            return None  # Retornar "None" caso o usuário aperte a tecla "ESC"
        webcam.release()  # Desligar a webcam
        cv2.destroyAllWindows()  # Fechar todas as janelas abertas pelo OpenCV

        return faces.detections
    
    def recognizeFace(self, image_path):
        print("Reconhecendo rostos...")

        image = cv2.imread(image_path)

        faces = self.faceDetector.process(image)

        if faces.detections:
            for face in faces.detections:
                self.drawing.draw_detection(image, face)
                cv2.imshow("Reconhecimento facial", image)
        else:
            return None

        # Para fechar a janela da webcam, basta apertar a tecla "ESC"
        if cv2.waitKey(5) == 27:
            return None  # Retornar "None" caso o usuário aperte a tecla "ESC"
        cv2.destroyAllWindows()  # Fechar todas as janelas abertas pelo OpenCV

        return faces.detections