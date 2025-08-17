# ReconhecimentoFacial

Sistema simples de cadastro, treinamento e reconhecimento facial utilizando OpenCV.

## Sumário

- [Descrição](#descrição)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como usar](#como-usar)
  - [1. Listar câmeras disponíveis](#1-listar-câmeras-disponíveis)
  - [2. Registrar rostos](#2-registrar-rostos)
  - [3. Treinar o reconhecedor](#3-treinar-o-reconhecedor)
  - [4. Reconhecer rostos](#4-reconhecer-rostos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Observações](#observações)

## Descrição

Este projeto permite registrar rostos de pessoas, treinar um modelo de reconhecimento facial e realizar o reconhecimento em tempo real utilizando webcam(s) conectadas ao computador.

## Pré-requisitos

- Python 3.x
- [OpenCV](https://opencv.org/) (`opencv-python` e `opencv-contrib-python`)
- Numpy

Instale as dependências com:

```sh
pip install opencv-python opencv-contrib-python numpy
```

## Instalação

Clone este repositório e coloque todos os arquivos na mesma pasta.

Certifique-se de que o arquivo `haarcascade_frontalface_default.xml` está presente na pasta do projeto.

## Como usar

### 1. Listar câmeras disponíveis

Execute o script para listar as câmeras conectadas ao seu computador:

```sh
python camerasDisponiveis.py
```

Anote o índice da câmera que deseja utilizar.

### 2. Registrar rostos

Execute o script para capturar imagens dos rostos que deseja cadastrar:

```sh
python ReconhecimentoFacialRegistrarFace.py
```

- Escolha a câmera desejada.
- Informe um ID numérico e o nome da pessoa.
- Serão capturadas até 100 imagens do rosto.
- Repita para cada pessoa que deseja cadastrar.

As imagens serão salvas na pasta `faces/` e o mapeamento de nomes em `names.json`.

### 3. Treinar o reconhecedor

Após cadastrar os rostos, treine o modelo:

```sh
python TreinamentoReconhecimentoFacial.py
```

O modelo treinado será salvo como `trainer.yml`.

### 4. Reconhecer rostos

Para iniciar o reconhecimento facial em tempo real:

```sh
python ReconhecimentoFinalFace.py
```

- Escolha a câmera desejada.
- O sistema exibirá o nome da pessoa reconhecida ou "Desconhecido" caso não seja identificado.
- Pressione `Q` para encerrar.

## Estrutura do Projeto

- `camerasDisponiveis.py`: Lista as câmeras disponíveis.
- `ReconhecimentoFacialRegistrarFace.py`: Captura e registra rostos.
- `TreinamentoReconhecimentoFacial.py`: Treina o modelo de reconhecimento facial.
- `ReconhecimentoFinalFace.py`: Realiza o reconhecimento facial em tempo real.
- `haarcascade_frontalface_default.xml`: Classificador Haar para detecção de rostos.
- `faces/`: Pasta onde as imagens dos rostos são salvas.
- `names.json`: Mapeamento de IDs para nomes.
- `trainer.yml`: Modelo treinado.

## Observações

- Certifique-se de que a iluminação do ambiente seja adequada para melhores resultados.
- Para adicionar novas pessoas, repita o processo de registro e re-treine o modelo.
- O reconhecimento depende da qualidade das imagens capturadas e do treinamento realizado.

---