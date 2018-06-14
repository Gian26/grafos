__author__ = 'ING26'
import pdb
"""
The Bellman-Ford algorithm
Graph API:
    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
"""

# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            if d[v] > (d[u] + graph[u][v]):
                print False
    return d, p


def test():
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
        }

    graph1= {'y': {'x': -3, 'z': 9},
             'x': {'t': -2},
             's': {'y': 7, 't': 6},
             'z': {'x': 7, 's': 2},
             't': {'y': 8, 'x': 5, 'z': -4}
             }

    d, p = bellman_ford(graph1, 's')
    print d,p



def popmin(pqueue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key

    del pqueue[keylowest]
    return keylowest

def prim(graph, root):
    pred = {} # pair {vertex: predecesor in MST}
    key = {}  # keep track of minimum weight for each vertex
    pqueue = {} # priority queue implemented as dictionary

    for v in graph:
        pred[v] = -1
        key[v] = 1000
    key[root] = 0
    for v in graph:
        pqueue[v] = key[v]
    print pqueue

    while pqueue:
        u = popmin(pqueue)
        print u
        for v in graph[u]: # all neighbors of v
            if v in pqueue and graph[u][v] < key[v]:
                pred[v] = u
                key[v] = graph[u][v]
                pqueue[v] = graph[u][v]
    return pred

graph1={'a': {'h': 8, 'b': 4}, 'c': {'i': 2, 'b': 8, 'd': 7, 'f': 4}, 'b': {'a': 4, 'h': 11, 'c': 8}, 'e': {'d': 9, 'f': 10}, 'd': {'c': 7, 'e': 9, 'f': 14}, 'g': {'i': 6, 'h': 1, 'f': 2}, 'f': {'c': 4, 'e': 10, 'd': 14, 'g': 2}, 'i': {'h': 7, 'c': 2, 'g': 6}, 'h': {'a': 8, 'i': 7, 'b': 11, 'g': 1}}

graph = {0 : {1:6, 2:8},
1 : {4:11},
2 : {3: 9},
3 : {},
4 : {5:3},
5 : {2: 7, 3:4}}
"""
pred = prim(graph1,"a")
for v in pred: print "%s: %s" % (v, pred[v])

print" BELLMAN-FORD"

test()

nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}
"""
nodes=('s','y','x','z','t')
distances={'y': {'x': 9, 'z': 2, 't': 3}, 'x': {'z': 4}, 's': {'y': 5, 't': 10}, 'z': {'x': 6, 's': 7}, 't': {'y': 2, 'x': 1}}

unvisited = {node: None for node in nodes} #using None as +in

visited = {}
current = 's'
currentDistance = 0
unvisited[current] = currentDistance


while True:
    for neighbour, distance in distances[current].items():

        if neighbour not in unvisited: continue

        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance

    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)