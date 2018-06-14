Materia: Matemáticas Discretas
Alumno: Gian Nestor Cuello Nicholson


Uso del programa:
----------------
Ejectura el siguiente comando en consola "python __init__.py".
Este archivo esta preparando con 6 ejemplos de los 6 diferentes algoritmos vistos en
clase del libro  "Introduction to Algorithms By Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein".

ALGORITMOS DE BUSQUEDA
-Algoritmo de busqueda por anchura: se crea un grafo no dirigido a partir del archivo BFS.txt
-Algoritmo de busqueda por profunidad: se crea un grafo dirigido a partir del archivo DFS.txt

MINIMUM SPANNING TREES
-Algoritmo MST-Kruskal : se crea un grafo dirigdo a partir del archivo primkrusk.txt
-Algoritmo MST-Prim : se crea un grafo dirigdo a partir del archivo primkrusk.txt

SINGLE SOURCE SHORTEST PATH
-Algoritmo Bellman-Ford: se crea un grafo dirigdo con pesos negativos a partir del archivo bellman.txt
-Algoritmo de Dijkstra: se crea un grafo dirigod con pesos no negativos a partir del archivo dijkstras.txt


Descripción de la clase Graph:
------------------------------
Al crear el objeto grafo se le indica que tipo de grafo va ser, dirigido o no dirigido. Se pasa el párametro al método costructor como un
valor booleano.

ej dirigido: dir_grafo = Graph(True)
ej no dirigido: no_dir_grafo = Graph(False)

Despues de crear el objeto grafo, se hace uso del método "read_file(archivo)" al cual le pasaremos una descripción del grafo
a generar. Ejemplos de diferentes grafos estan incluidos.

ej: dir_grafo.read_file("DFS.txt")


Métodos de los diferentes algoritmos:
------------------------------------

bfs(source) : Algoritmo de busqueda por anchura. Tiene como parámetro el vertice de inicio para recorrer el grafo.
dfs(): No tiene parámetros. Empieza desde cualquier nodo y hace un recorrido de todos los nodos adyacentes del nodo descubierto.

MST_Kruskal(): No tiene parámetros. Reordena todos los aristas del grafo de menor a mayor, va agregando nodos al árbol si estos no crean un ciclo.
MST_Prim(source): Recibe como parametro un vertice. Partiendo del vertice y haciendo uso de una cola de prioridades va generando un MST.

bellman_ford(source): Inicia desde un vertice, y determina el camino más corto para llegar a todos los demás vertices, considerando pesos negativos.
dijkstras(source): Inicia desde un vertice y determina el camino más corto para llegar a todos los demás vertices, no considera pesos negativos.