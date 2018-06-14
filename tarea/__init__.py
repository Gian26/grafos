__author__ = 'ING26'
from grafo import *
# heapsort
if __name__ == "__main__":
    print
    g_no = Graph(False)
    g_no.read_file("BFS.txt")
    print "Busqueda por anchura (BFS): "
    print "Partiendo del nodo s."
    pi,d,color = g_no.bfs("s")
    print "Lista de vertices con sus padres: ",pi
    print "distancias: ",d
    print

    g_dir = Graph(True)
    g_dir.read_file("DFS.txt")
    print "Busqueda por profundidad (DFS):"
    d,f,pi=g_dir.dfs()
    print "Tiempo incial de los vertices: ",d
    print "Tiempo final de los vertices: ",f
    print "Listsa de vertices con sus padres: ",pi
    print

    kruskal = Graph(False)
    kruskal.read_file("primkrusk.txt")
    print "Minimu spanning tree kruskal: "
    aristas,peso= kruskal.MST_Kruskal()
    print "Aristas del arbol: ",aristas
    print "Peso total del MST: ", peso
    print

    prim = Graph(False)
    prim.read_file("primkrusk.txt")
    print "Minimum spanning tree Prim : "
    print "Partiendo del vertice a"
    pesos,predecesores,peso=prim.MST_Prim("a")
    print "Los costos de cada arista",pesos
    print "Lista de vertices y sus padres",predecesores
    print "Peso total del arbol:",peso
    print

    bf = Graph(True)
    bf.read_file("bellman.txt")
    print "Single source shortest-path Bellman-Ford Algorithm: "
    print "Partiendo del vertice s."
    pesos,pi=bf.bellman_ford("s")
    print "Lista de vertices y sus padres: ", pi
    print "Lista de vertices con su costo: ", pesos
    print

    dj = Graph(True)
    dj.read_file("dijkstras.txt")
    print "Single source shortes-path Dijkstra's algorithm"
    pi,S=dj.dijkstras("s")
    print "Paritendo del vertice s"
    print "Lista de vertices con sus predecesores",pi
    print "Lista de vertices y su costo: ",S
