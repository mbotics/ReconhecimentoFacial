import cv2
import numpy as np
import os
from config import *

print("\nIniciando treinamento...")

path = 'faces'
if not os.path.exists(path) or not os.listdir(path):
    print("Erro: Pasta 'faces' vazia ou não encontrada!")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def get_images_and_labels(path):
    face_samples = []
    ids = []

    # Percorre todas as pastas de pessoas
    for pessoa_dir in os.listdir(path):
        if not os.path.isdir(os.path.join(path, pessoa_dir)):
            continue
            
        # Extrai o ID da pessoa do nome da pasta
        try:
            id = int(pessoa_dir.split('_')[0])
        except:
            continue
            
        pessoa_path = os.path.join(path, pessoa_dir)
        
        # Processa cada imagem da pasta da pessoa
        for image_file in os.listdir(pessoa_path):
            if not image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue
                
            image_path = os.path.join(pessoa_path, image_file)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            
            if img is not None:
                face_samples.append(img)
                ids.append(id)

    return face_samples, ids

print("Processando imagens...")
faces, ids = get_images_and_labels(path)

if not faces:
    print("Erro: Nenhum rosto detectado nas imagens!")
    exit()

print(f"Total de amostras: {len(faces)}")
print(f"Pessoas identificadas: {len(np.unique(ids))}")

print("Treinando reconhecedor...")
recognizer.train(faces, np.array(ids))
recognizer.write('trainer.yml')

print("Treinamento concluído! Modelo salvo como 'trainer.yml'")