import cv2
import numpy as np
import json
import os

def selecionar_camera():
    """Permite ao usuário selecionar qual câmera usar"""
    index = 0
    cameras = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            cameras.append(index)
        cap.release()
        index += 1
    
    if not cameras:
        print("Nenhuma câmera encontrada!")
        exit()
    
    print("\nCâmeras disponíveis:")
    for i, cam_idx in enumerate(cameras):
        print(f"{i} -> Índice {cam_idx}")
    
    while True:
        try:
            escolha = int(input("Digite o número da câmera que deseja usar: "))
            if 0 <= escolha < len(cameras):
                return cameras[escolha]
            print("Número inválido! Tente novamente.")
        except ValueError:
            print("Digite apenas números!")

# Carrega o modelo treinado
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Carrega o mapeamento de IDs para nomes
names = {}
if os.path.exists('names.json'):
    with open('names.json', 'r') as f:
        names = json.load(f)

# Seleciona a câmera
camera_idx = selecionar_camera()
cap = cv2.VideoCapture(camera_idx)
cap.set(3, 640)
cap.set(4, 480)

print("\nReconhecimento ativo. Pressione Q para sair")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar frame!")
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        
        id, confidence = recognizer.predict(face_roi)
        
        if confidence < 60:
            name = names.get(str(id), f"Convidado {id}")  # Convertendo para string pois JSON usa strings como chaves
            color = (0, 255, 0)  # Verde para conhecidos
        else:
            name = "Desconhecido"
            color = (0, 0, 255)  # Vermelho para desconhecidos
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, f"{name} ({confidence:.1f})", 
                   (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow('Reconhecimento Facial', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Programa encerrado")