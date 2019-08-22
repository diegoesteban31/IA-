import pygame
import sys
from pygame.locals import *

Rosa = (255,0,128)
Verde = (0,128,0)
Amarillo = (255,255,0)
Rojo = (255,0,0)
Blanco = (255,255,255)
Negro = (0,0,0)
Naranja = (255,164,32)
Morado = (87,35,100)
Cafe = (141,73,37)
Gris = (156,156,156)
Plateado = (138,149,151)
Dorado = (212,175,55)
Esmeralda = (0,157,113)
Turquesa = (93,193,185)
Magenta = (229,9,127)
Lila = (182,149,192)
Violeta = (76,40,130)
Beige = (245,245,220)
Crema = (248,222,129)
Mostaza = (255,219,88)

colores = [Rosa,Verde,Amarillo,Rojo,Blanco,Negro,Naranja,Morado,Cafe,Gris,Plateado,
            Dorado,Esmeralda,Turquesa,Magenta,Lila,Violeta,Beige,Crema,Mostaza]

colorR = (255, 255, 255, 255)


pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("MY OWN PAINT")

color = pygame.Color(255,255,255)
window.fill(color)

color2 = pygame.Color(0,0,0)
for x in range(30):
    posx = x*30
    pygame.draw.line(window,color2,(posx,0),(posx,600))
for y in range(30):
    posy = y*30
    pygame.draw.line(window,color2,(0,posy),(600,posy))

rectan = pygame.Surface((30, 30))       #Tamano del Rectangulo
for x in range(len(colores)):
    posx = x*30
    rectan.fill(colores[x])
    window.blit(rectan, (posx, 0))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    if evento.type == pygame.MOUSEBUTTONDOWN:
        if evento.button == 1:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            pos1 = int(mouse_x/30)
            pos1 = pos1*30
            pos2 = int(mouse_y/30)
            pos2 = pos2*30
            if pos2 > 0:
                rectan.fill(colorR)
                window.blit(rectan, (pos1, pos2))
        elif evento.button == 3:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            colorR = window.get_at((mouse_x,mouse_y))
            print(colorR)

    pygame.display.update()
