import pygame
import os
import time
from pygame.locals import *
from ast import literal_eval

class Problem():
    def __init__(self, namefile):

        self.Verde = (0,255,0)
        self.Rojo = (255,0,0)
        self.Negro = (0,0,0)
        self.Azul = (0,0,255)

        self.colorR = (255, 255, 255, 255)
        self.rectan = pygame.Surface((20, 20))

        #Manejo de Archivo
        self.wall = []
        file = open(namefile,"r")
        self.start = literal_eval(file.readline())
        self.goal = literal_eval(file.readline())
        for line in file:
            self.wall.append(literal_eval(line))

        # Dibujando Mapa
        pygame.init()
        self.window = pygame.display.set_mode((600,600))
        pygame.display.set_caption("Game")

        color = pygame.Color(255,255,255)
        self.window.fill(color)

        color2 = pygame.Color(0,0,0)
        for x in range(30):
            posx = x*20
            pygame.draw.line(self.window,color2,(posx,0),(posx,600))
        for y in range(30):
            posy = y*20
            pygame.draw.line(self.window,color2,(0,posy),(600,posy))

        x = int(self.goal[0])*20
        y = int(self.goal[1])*20
        self.rectan.fill(self.Verde)
        self.window.blit(self.rectan, (x,y))
        x = int(self.start[0])*20
        y = int(self.start[1])*20
        self.rectan.fill(self.Rojo)
        self.window.blit(self.rectan, (x,y))
        for pos in self.wall:
            x = int(pos[0])*20
            y = int(pos[1])*20
            self.rectan.fill(self.Negro)
            self.window.blit(self.rectan, (x,y))

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return self.goal == state


def Explore(Node, Cost, Route):
    Aux_Rut = []
    Aux = []
    x = (Node[0]*20)+10
    y = (Node[1]*20)+10
    Cost+=1
    for N in Route:
        Aux_Rut.append(N)
    Aux_Rut.append(Node)
    for Move in Pos:
        aux_x = x+Move[0]
        aux_y = y+Move[1]
        if aux_x>0 and aux_x<600 and aux_y>0 and aux_y<600:
            if window.get_at((aux_x,aux_y)) == Blanco or window.get_at((aux_x,aux_y)) == (0,255,0,255):
                dic = {'Pos':((aux_x-10)/20,(aux_y-10)/20),'Rut':Aux_Rut,'Cost': Cost}
                Aux.append(dic)
    return Aux

def graph_search(Problema,Estrategia):
    Explorados = []
    Cost = 0
    Front = [{'Pos': Problema.getStartState(),'Rut':[],'Cost': 0}]
    while Front:
        Cost,u,Ruta = Front.pop().values()
        # print("Posicion: "+str(u))
        # print("Ruta: "+str(Ruta))
        # print("Costo: "+str(Cost))
        if Problema.isGoalState(u):
            print("Termino: "+str(Ruta))
            #print("Frontera: "+str(Front))
            #print("Explorados: "+str(Explorados))
            print("Costo: "+str(Cost))
            return Ruta, Cost
        if not u in Explorados:
            # print("Explorando: ",str(u))
            Aux = Explore(u,Cost,Ruta)
            if Estrategia == "LIFO":
                Front+=Aux
            elif Estrategia == "FIFO":
                for dic in Aux:
                    Front.insert(0,dic)
            Explorados.append(u)
            #Pintando
            x = int(u[0])*20
            y = int(u[1])*20
            rectan.fill(Azul)
            window.blit(rectan, (x,y))
            pygame.display.update()
            time.sleep(0.01)
    print("Frontera Vacia")

#Variables
N = [0,-20]
S = [0,20]
O  = [20,0]
W = [-20,0]
Pos = [N,S,O,W]
window = pygame.display.set_mode((600,600))
Blanco = (255,255,255,255)
rectan = pygame.Surface((20, 20))
Azul = (0,0,255)
Naranja = (255,164,32)

problema = Problem("./juego.txt")
ruta, costo = graph_search(problema,"FIFO")
#Pinta Ruta
for pos in ruta:
    x = int(pos[0])*20
    y = int(pos[1])*20
    rectan.fill(Naranja)
    window.blit(rectan, (x,y))

#Pinta Inicio
print(problema.getStartState())
x = int(problema.getStartState()[0])*20
y = int(problema.getStartState()[1])*20
rectan.fill((255,0,0))
window.blit(rectan, (x,y))
pygame.display.update()

while  True:
    evento = pygame.event.wait()
    if evento.type == pygame.QUIT:
        break
    pygame.display.update()
