__author__ = 'ING26'
from grafo import *
from sets import *
class dirigdo(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.time = 0


    def lista_esquinas(self):
        edges = []
        graph = self.vertices
        for node in graph:
            for neighbour in graph[node]:
                edges.append(( node ,neighbour))
        return edges

    def read_file(self,archivo):
        tf = open(archivo, "r")
        s=tf.readline()     #leemos la primera linea
        list=s.lstrip().rstrip().split(' ') #Eliminamos espacios y caracteres no imprimible en los extremos y extraemos tokens
        cardV=int(list[0])
        cardMaxA = cardV*(cardV+1)/2
        cardA=int(list[1])
        idList=[]
        if cardA > cardMaxA:
            print "Error: numero de aristas demasiado grande."
            return [[], [], 0]
        for i in range(cardV):
            s=tf.readline()     #Leemos linea
            a=s.lstrip().rstrip() #eliminamos espacio y caracteres no imprimibles en los extremos.
            idList.append(a)    #Agregamos identificador de vertice a lista
        arista = []
        for i in range(cardA):
            s=tf.readline()     #leemos la primera linea
            ln=s.lstrip().rstrip().split(' ')#Eliminamos espacios y caracteres no imprimible en los extremos y extraemos tokens
            arista.append(ln)
        #print arista , cardV ,len(arista)

        for i in range(0,cardV):
            dicto={}#set()
            for j in range(0,len(arista)):
                if idList[i] ==arista[j][0] and idList[i] == arista[j][1]:
                    dicto[idList[i]]=int(arista[j][2])
                if idList[i] ==arista[j][0] and idList[i] != arista[j][1]:
                    dicto[arista[j][1]]=int(arista[j][2])

            self.agregar_nodo(idList[i], dicto)


    def DFS(self):
        self.color={}
        self.pi= {}
        self.d={}
        self.f={}
        for u in self.vertices:
            self.pi[u]=None
            self.color[u]="blanco"
        self.time = 0
        for u in self.vertices:
            if self.color[u] == "blanco":
                self.DFS_visit(u)
        print self.d
        print self.f

    def DFS_visit(self,u):
        self.time = self.time +1
        self.d[u] = self.time
        self.color[u] = "gris"
        for v in self.vertices[u]:
            if self.color[v] == "blanco":
                self.pi[v] =u
                self.DFS_visit(v)
        self.color[u] ="black"
        self.time += 1
        self.f[u] = self.time

