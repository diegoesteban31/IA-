import pygame
import os
import time
import argparse
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

def uniformCostSearch(Frontera, No_Explorados):
    Frontera+=No_Explorados
    Frontera.sort()
    Frontera.reverse()
    return Frontera

def graph_search(Problema,Estrategia):
    Explorados = []
    Cost = 0
    Front = [{'Pos': Problema.getStartState(),'Rut':[],'Cost': 0}]
    while Front:
        Cost,u,Ruta = Front.pop().values()
        if Problema.isGoalState(u):
            return Ruta, Cost, len(Explorados)
        if not u in Explorados:
            Aux = Explore(u,Cost,Ruta)
            if Estrategia == "DFS":
                Front+=Aux
            elif Estrategia == "BFS":
                for dic in Aux:
                    Front.insert(0,dic)
            elif Estrategia == "UCS":
                Front = uniformCostSearch(Front, Aux)
            else:
                print("Estrategia Desconocido")
                return 0,0,0
            Explorados.append(u)
            #Pintando
            x = int(u[0])*20
            y = int(u[1])*20
            rectan.fill(Azul)
            window.blit(rectan, (x,y))
            pygame.display.update()
            time.sleep(0.01)
    print("Frontera Vacia")

#Argumento por consola
parser = argparse.ArgumentParser()
parser.add_argument("strategy", help="Select the strategy for search")
args = parser.parse_args()

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
Esmeralda = (0,157,113)
start_time = time.time()

strategy = args.strategy
problema = Problem("./juego.txt")
ruta, costo, explorados = graph_search(problema,strategy)
elapsed_time = time.time() - start_time

#Texto en el juego
cost_text = "Costo: "+str(costo)
state_explore = "Estados explorados: "+str(explorados)
estratregia = "Estrategia "+strategy
time = "Tiempo: "+str(elapsed_time)+" seg"
myfont = pygame.font.SysFont('Noto Sans CJK KR Black', 30)

#Pinta Ruta
for pos in ruta:
    x = int(pos[0])*20
    y = int(pos[1])*20
    rectan.fill(Naranja)
    window.blit(rectan, (x,y))

#Pinta Inicio
x = int(problema.getStartState()[0])*20
y = int(problema.getStartState()[1])*20
rectan.fill((255,0,0))
window.blit(rectan, (x,y))
pygame.display.update()

while  True:
    evento = pygame.event.wait()
    if evento.type == pygame.QUIT:
        break

    textsurface = myfont.render(cost_text, False, Esmeralda)
    window.blit(textsurface,(0,520))
    textsurface = myfont.render(state_explore, False, Esmeralda)
    window.blit(textsurface,(0,480))
    textsurface = myfont.render(estratregia, False, Esmeralda)
    window.blit(textsurface,(0,400))
    textsurface = myfont.render(time, False, Esmeralda)
    window.blit(textsurface,(0,440))
    pygame.display.update()
