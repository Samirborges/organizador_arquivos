import os
import shutil

# Defindo os diretórios
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, "OneDrive", "Área de Trabalho")

CAMINHO_ARQUIVO_ORGANIZADOR = os.path.join(DESKTOP, "Organizador")
CAMINHO_ARQUIVO_IMAGENS = os.path.join(DESKTOP, "Imagens")
CAMINHO_ARQUIVO_VIDEOS = os.path.join(DESKTOP, "Vídeos")


for root, dirs, files in os.walk(CAMINHO_ARQUIVO_ORGANIZADOR):
    for file in files:
        index_point_extension = file.index('.')
        extension_file = file[index_point_extension:]
        
        caminho_arquivo = os.path.join(root, file)
        if extension_file == '.mp4':
            caminho_arquivo_organizador_video = os.path.join(
                CAMINHO_ARQUIVO_VIDEOS, file
            )
            shutil.move(caminho_arquivo, caminho_arquivo_organizador_video)
            
        if extension_file == '.jpg':
            caminho_arquivo_organizador_imagem = os.path.join(
                CAMINHO_ARQUIVO_IMAGENS, file
            )
            shutil.move(caminho_arquivo, caminho_arquivo_organizador_imagem)
        