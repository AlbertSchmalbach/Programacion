import pygame

# Inicializar pygame
pygame.init()

# Ruta del archivo de audio
ruta_archivo_audio = r"C:\Users\KHAdmin\Documents\CarpetaProtegida\audio.mp3"

# Inicializar el reproductor de audio
pygame.mixer.init()

# Cargar el archivo de audio
pygame.mixer.music.load(ruta_archivo_audio)

# Reproducir el audio
pygame.mixer.music.play()

# Esperar hasta que se termine de reproducir
while pygame.mixer.music.get_busy():
    pass

# Detener pygame
pygame.quit()
