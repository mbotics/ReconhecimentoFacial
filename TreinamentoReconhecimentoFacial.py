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
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        id = int(os.path.split(image_path)[-1].split('_')[1])
        # Usa a imagem já redimensionada diretamente
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