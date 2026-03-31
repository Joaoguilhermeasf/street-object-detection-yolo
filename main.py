import cv2
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("URL")

import cv2

cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)
print("Opened:", cap.isOpened())

ret, frame = cap.read()

if ret:
    cv2.imwrite("frame.jpg", frame)
    print("Frame capturado da URL 🚀")
else:
    print("Erro ao capturar frame da URL")

cap.release()