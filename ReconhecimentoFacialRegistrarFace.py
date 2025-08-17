import cv2
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

def capturar_rostos(camera_idx):
    # Configurações iniciais
    if not os.path.exists('faces'):
        os.makedirs('faces')

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    if face_cascade.empty():
        print("Erro: Classificador Haar não carregado!")
        return

    cap = cv2.VideoCapture(camera_idx)
    cap.set(3, 640)  # largura
    cap.set(4, 480)  # altura

    face_id = input("\nDigite um ID numérico para a pessoa: ")
    count = 0

    print("\nCapturando rostos... Pressione Q para encerrar")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar frame!")
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            count += 1
            cv2.imwrite(f"faces/face_{face_id}_{count}.jpg", gray[y:y+h, x:x+w])
            print(f"Capturada imagem {count}/100", end='\r')

        cv2.imshow('Capturando Rostos', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 100:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"\nCaptura concluída! {count} imagens salvas na pasta 'faces'")

# Programa principal
def main():
    # Seleciona a câmera uma única vez
    camera_idx = selecionar_camera()
    
    while True:
        capturar_rostos(camera_idx)
        
        resposta = input("\nDeseja cadastrar outra pessoa? (s/n): ").lower()
        if resposta != 's':
            print("Encerrando o programa...")
            break

if __name__ == "__main__":
    main()