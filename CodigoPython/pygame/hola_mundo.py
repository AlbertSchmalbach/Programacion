# Example file showing a basic pygame "hola mundo"
import pygame, sys
from pygame.locals import *

# Colors
# color = (0, 140, 60)
# color2 = pygame.Color(180,120,40)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('pygame')
running = True

# lines
color = pygame.Color(70, 80, 150)
# line(ventana, color, (x0, y0), (xf, yf), grosor)
pygame.draw.line(screen, color, (60, 80), (200, 80), 5)

print(color.r)
print(color.g)
print(color.b)

while running:
    # screen background
    # screen.fill(color2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
    pygame.display.update()

