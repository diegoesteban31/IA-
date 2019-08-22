import pygame
import os
from pygame.locals import *

Rosa = (255,0,128)
Verde = (0,255,0)
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
wall = []
file = open("./juego.txt","w")

pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption("MY OWN PAINT")

color = pygame.Color(255,255,255)
window.fill(color)

color2 = pygame.Color(156,156,156)
for x in range(30):
    posx = x*20
    pygame.draw.line(window,color2,(posx,0),(posx,600))
for y in range(30):
    posy = y*20
    pygame.draw.line(window,color2,(0,posy),(600,posy))

rectan = pygame.Surface((20, 20))       #Tamano del Rectangulo
for x in range(len(colores)):
    posx = x*20
    rectan.fill(colores[x])
    window.blit(rectan, (posx, 0))

while True:
    evento = pygame.event.wait()

    if evento.type == pygame.QUIT:
        break

    ## Dibujando el mapa
    if evento.type == pygame.MOUSEBUTTONDOWN:
        if evento.button == 1:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            pos1 = int(mouse_x/20)
            pos1 = pos1*20
            pos2 = int(mouse_y/20)
            pos2 = pos2*20
            if pos2 > 0:
                rectan.fill(colorR)
                window.blit(rectan, (pos1, pos2))
        elif evento.button == 3:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            colorR = window.get_at((mouse_x,mouse_y))
            print(colorR)

    ## Barriendo el mapa
    if evento.type == pygame.KEYDOWN:
        tecla = pygame.key.name(evento.key)
        print(tecla)
        if (tecla == 'escape'):
            print("entre hijueputas")
            for x in range(20, 600,20):         #horizontal
                for y in range(40, 600,20):     #vertical
                    colorPix = window.get_at((x,y))
                    if colorPix == (255, 0, 0, 255):
                        start = x/20,y/20
                        print ("Rojo: "+str(start))
                    elif colorPix == (0, 255, 0, 255):
                        goal = x/20,y/20
                        print("Verde: "+str(goal))
                    elif colorPix == (0, 0, 0, 255):
                        wall.append((x/20,y/20))
            print("Pared: "+str(wall))
            file.write(str(start)+os.linesep)
            file.write(str(goal)+os.linesep)
            for coordenadas in wall:
                file.write(str(coordenadas)+os.linesep)
            file.close()

    pygame.display.update()
