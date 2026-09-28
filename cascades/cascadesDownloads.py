import os
import urllib.request
import cv2

# Cria uma pasta 'cascades' no seu projeto, se não existir
PASTA_CASCADES = 'cascades'
os.makedirs(PASTA_CASCADES, exist_ok=True)

# Lista dos principais classificadores
arquivos_xml = [
    'haarcascade_frontalface_default.xml',
    'haarcascade_frontalface_alt.xml',
    'haarcascade_eye.xml',
    'haarcascade_smile.xml'
]

BASE_URL = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/'

# Download automático dos arquivos para a pasta local
for xml in arquivos_xml:
    caminho_local = os.path.join(PASTA_CASCADES, xml)
    if not os.path.exists(caminho_local):
        print(f"Baixando {xml}...")
        urllib.request.urlretrieve(BASE_URL + xml, caminho_local)

print("Download concluído! Todos os arquivos estão na pasta 'cascades/'.")