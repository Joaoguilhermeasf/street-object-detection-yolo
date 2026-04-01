import cv2
from ultralytics import YOLO
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()
url = os.getenv("URL")

# Carrega modelo YOLO (leve e rápido)
model = YOLO("yolov8n.pt")

# Captura de vídeo
cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)

print("Câmera aberta:", cap.isOpened())

while True:
    ret, frame = cap.read()

    if not ret:
        print("Erro ao capturar frame")
        break

    # 🔥 DETECÇÃO COM YOLO
    results = model(frame)

    # Desenha caixas na imagem
    annotated_frame = results[0].plot()

    # Mostra na tela
    cv2.imshow("Detecção YOLO", annotated_frame)

    # Tecla 'q' para sair
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Finaliza tudo
cap.release()
cv2.destroyAllWindows()