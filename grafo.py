__author__ = 'ING26'
from min_priority_queue import *
class Graph:
    def __init__(self,tipo):
        self.tipo = tipo
        self.grafo = {'Nodo_1': {'Nodo_3': 15.0, 'Nodo_0': 15.0}, 'Nodo_2': {'Nodo_3': 15.0, 'Nodo_0': 15.0}, 'Nodo_3': {'Nodo_1': 15.0, 'Nodo_2': 15.0}, 'Nodo_0': {'Nodo_1': 15.0, 'Nodo_2': 15.0}}
        self.parent ={}
        self.rank={}

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

        if(not self.tipo):
            print self.tipo
            for i in range(0,cardV):
                dicto={}
                for j in range(0,len(arista)):
                    if idList[i] ==arista[j][0] and idList[i] == arista[j][1]:
                        dicto[idList[i]]=(arista[j][2])
                    if idList[i] !=arista[j][0] and idList[i] == arista[j][1]:
                        dicto[arista[j][0]]=(arista[j][2])
                    if idList[i] ==arista[j][0] and idList[i] != arista[j][1]:
                        dicto[arista[j][1]]=(arista[j][2])
                self.agregar_nodo(idList[i], dicto)
        else:
            for i in range(0,cardV):
                dicto={}#set()
                for j in range(0,len(arista)):
                    if idList[i] ==arista[j][0] and idList[i] == arista[j][1]:
                        dicto[idList[i]]=float(arista[j][2])
                    if idList[i] ==arista[j][0] and idList[i] != arista[j][1]:
                        dicto[arista[j][1]]=float(arista[j][2])
                self.agregar_nodo(idList[i], dicto)

    def vertices(self):
      return self.grafo.keys()

    def adj(self,v):
      return self.grafo[v].keys()

    def adyacentes(self,v):
        vecinos = self.grafo[v[1]]
        aristas = []
        for letter in vecinos:
            aristas.append((vecinos[letter],v[1],letter))
        return aristas

    def w(self,u,v):
      return self.grafo[u][v]

    def aristas(self):
        edges = []
        graph = self.grafo
        for node in graph:
            for neighbour in graph[node]:
                edges.append((graph[node][neighbour], node ,neighbour))
        return edges

    def agregar_nodo(self, name, edges):
        self.grafo[name] = edges

    def agregar_helper(self,nodoA,nodoB,valor):
        elemento = self.vertices[nodoA]
        elemento.update({nodoB:valor})
        self.grafo.update({nodoA:elemento})

    def agregar_arista(self,arista):
        if arista[0] in self.grafo:
            if arista[1] in self.grafo:
                self.agregar_helper(arista[0],arista[1],arista [2])
                self.agregar_helper(arista[1],arista[0],arista [2])
            else:
                print "nodo " + arista[1]+" no existe."
        else:
            print "nodo " + arista[0]+" no existe."

    def __str__(self):
        return str(self.grafo)

    ##ALGORITMOS DE BUSQUEDA
    # BUSQUEDA POR ANCHURA, BUSQUEDA POR PROFUNIDAD
    ########################## ALGORITMOS DE ANCHURA  ##############################
    def bfs(self,s):
        d={}   # distancia
        pi={} # predecesor de u
        color= {} # el color del vertice

        #inicializamos  los atributos a utilizar para la busqueda
        for v in self.grafo:
            if s != v:
                d[v]=0
                pi[v]=None
                color[v]="blanco"

        # inicializamos el nodo de inicio
        d[s]=0
        color[s]="gris"
        pi[s]=None

        # creamos una cola y le insertamos el nodo inicial
        q=[]
        q.append(s)

        while len(q) > 0:
            u = q[0]
            del q[0] # quita el elemento en la cabeza de la cola
            for v in self.grafo[u]: # revisar los vecinos de u
                if color[v] =="blanco":
                    d[v] = d[u] + 1 # incrementamos la distancia de v apartir de u
                    pi[v]= u    # el predecesor de v es u
                    color[v]="gris" # como fue visitado, se cambia a gris
                    q.append(v) # ahora metemos v a la cola
            color[u]="black"
        return pi,d,color

    ########################ALGORITMO DE PROFUNIDAD#################################
    def dfs(self):
        self.color={}
        self.pi= {}
        self.d={} # inicio
        self.f={} # fin
        for u in self.grafo:
            self.pi[u]=None
            self.color[u]="blanco"
        self.time = 0
        for u in self.grafo:
            if self.color[u] == "blanco":
                self.__dfs_visit(u)
        return self.d, self.f, self.pi

    def __dfs_visit(self,u):
        self.time = self.time +1
        self.d[u] = self.time
        self.color[u] = "gris"
        for v in self.grafo[u]:
            if self.color[v] == "blanco":
                self.pi[v] =u
                self.__dfs_visit(v)
        self.color[u] ="negro"
        self.time += 1
        self.f[u] = self.time

    ### MINIMUM SPANNING TREES
    # MST-KRUSKAL , MST-PRIM
    #################################ALGORITMO DE KRUSKAL############################################
    def __make_set(self,vertice):
        self.parent[vertice] = vertice
        self.rank[vertice] = 0

    def __union(self,vertice1, vertice2):
        self.__link( self.__find_set(vertice1),self.__find_set(vertice2))

    #retorna la raiz
    def __find_set(self,vertice):
        if self.parent[vertice] != vertice:
            self.parent[vertice] = self.__find_set(self.parent[vertice])
        return self.parent[vertice]

    def __link(self,vertice1,vertice2):
        if vertice1 != vertice2:
            if self.rank[vertice1] > self.rank[vertice2]:
                self.parent[vertice2] = vertice1
            else:
                self.parent[vertice1] = vertice2
                if self.rank[vertice1] == self.rank[vertice2]:
                    self.rank[vertice2] += 1

    def MST_Kruskal(self):
        spanning_Arbol = []
        for v in self.grafo:
            self.__make_set(v)
        esquinas = sorted(self.aristas())

        for esquina in esquinas:
            #verifica los vertices del arista
            if self.__find_set(esquina[1])!= self.__find_set(esquina[2]): # verificar si no estan en el mismo arbol
                spanning_Arbol.append(esquina) # agrega esquina al arbol
                self.__union(esquina[1],esquina[2]) # combina los arboles arbol

        return spanning_Arbol,self.__MSTw(spanning_Arbol)

    def __MSTw(self,A):
        sum=0
        for i in A:
            sum+= i[0]
        return sum
    ##################################ALGORITMO PRIM ####################################################
    def MST_Prim(self, root):
        pi = {}
        d = {}
        A=[]
        cola = []
        for v in self.grafo:
            pi[v] = -1
            d[v] = 1000

        d[root] = 0
        cola.append((0,0))
        for v in self.grafo:
            cola.append((d[v],v))

        pq =   min_priorityQueue()
        pq.build_min_heap(cola)
        cola=pq.get_heap()

        while cola:
            u = pq.heap_Extract_Minimum()
            A.append(u)
            cola=pq.get_heap()
            for v in self.grafo[u[1]]:
                key = pq.heap.index((d[v],v))
                if self.__checkExistence(v,cola) and self.grafo[u[1]][v] < d[v]:
                    pi[v] = u[1]
                    d[v] = self.grafo[u[1]][v] #decrease key implicito...
                    pq.heap_decrease_key(key,(d[v],v))
                cola = pq.get_heap()

        return d,pi,self.__MSTw(A)

    def __checkExistence(self,v,cola):
        for i in cola:
            if v == i[1]:
                return True
        return False


    #### SINGLE SOURCE SHORTEST PATH
    ### BELMAN-FORD, DIJKSTRA
    #######################################ALGORITMO BELMAN-FORD##################################################
    def initialize_single_source(self,source):
        d={}
        pi={}
        for v in self.vertices():
            d[v]=999999999999.0
            pi[v]=None

        d[source]=0

        return d,pi

    def __relax(self,u,v,d,pi):
        print d[u] ," ", self.w(u,v)
        print d[v], " ",d[u] + self.w(u,v)  
        if d[v]> d[u]+ self.w(u,v): # si el camino que se tiene es mayor que el encontrado sustituir
            d[v]=d[u]+self.w(u,v) # la distancia
            pi[v]= u                #predecesor

    def bellman_ford(self,s):
        d,pi=self.initialize_single_source(s)
        for i in range(0,len(self.vertices())-1): # v - 1 iteraciones
            for i in self.aristas():
                self.__relax(i[1],i[2],d,pi)

        for i in self.aristas(): # verificar si existe un ciclo negativo
            if d[i[2]] > d[i[1]] + self.w(i[1],i[2]):
                return "Se encontro un ciclo negativo"
        return d,pi

    #############################################ALGORITMO DIJKSTRA#############################################
    def dijkstras(self,s):
        d,pi=self.initialize_single_source(s)
        S = []

        cola = []
        cola.append((0,0))
        for v in self.grafo:
            cola.append((d[v],v))
        pq =   min_priorityQueue()
        pq.build_min_heap(cola)
        cola = pq.get_heap()

        #elementos en la cola
        while cola:
            #retirar el elemento mas pequeno
            u= pq.heap_Extract_Minimum()
            S.append(u) # Resultado, contiene los aristas del arbol encontrado

            for v in self.adj(u[1]): #obtener los vecinos de u
                u1 = u[1]
                key = pq.heap.index((d[v],v))
                #relax
                if d[v] > (d[u1]+ self.w(u1,v)):
                    d[v]=d[u1]+self.w(u1,v)
                    pi[v]= u1
                    pq.heap_decrease_key(key,(d[v],v))
                cola = pq.get_heap() # actualizar la cola

        return pi,S