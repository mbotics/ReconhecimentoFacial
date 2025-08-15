import cv2

def listar_cameras():
    """
    Detecta e lista todas as câmeras disponíveis no sistema
    Retorna uma lista com os índices das câmeras encontradas
    """
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
    return cameras

if __name__ == "__main__":
    cams = listar_cameras()
    if not cams:
        print("Nenhuma câmera encontrada!")
    else:
        print("\nCâmeras disponíveis:")
        for i, cam_idx in enumerate(cams):
            print(f"{i} -> Índice {cam_idx}")
        
        print("\nDica: Use o índice numérico no script de captura/reconhecimento")