import pygame
import os

# Inicializa o mixer do Pygame
pygame.init()

# Define o caminho para o arquivo de áudio
caminho_arquivo = os.path.join('tomp3.cc - Gabriel Henrique  Hallelujah Cover Acoustic.mp3')

# Carrega o arquivo de áudio
pygame.mixer.music.load(caminho_arquivo)

# Reproduz o arquivo de áudio
pygame.mixer.music.play()

# Espera o evento de encerramento
pygame.event.wait()



while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(100)