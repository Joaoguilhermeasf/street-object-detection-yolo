import cv2
import os
from dotenv import load_dotenv
from ultralytics import YOLO

# Carrega .env
load_dotenv()
url = os.getenv("URL")

if not url:
    print("Erro: URL não encontrada no .env")
    exit()

# Abre o stream
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Erro ao abrir o stream")
    exit()

# Carrega modelo YOLO leve
model = YOLO("yolov8n.pt")

print("Rodando detecção em tempo real... (pressione 'q' para sair)")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Erro ao capturar frame")
        break

    # (Opcional) Reduz tamanho pra ganhar performance
    frame = cv2.resize(frame, (720, 480))

    # Detecção
    results = model(frame)

    # Desenha caixas
    annotated_frame = results[0].plot()

    # Mostra na tela
    cv2.imshow("YOLO Stream", annotated_frame)

    # Sai ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()