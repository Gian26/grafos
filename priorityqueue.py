__author__ = 'G26'

class priorityQueue:
    def __init__(self):
        self.heap = []
        self.heap_size=0

    def parent(self,i):
        return i / 2

    def left(self,i):
        return i * 2

    def right(self,i):
        return self.left(i) + 1

    def get_heap(self):
        return self.heap[1:]

    def get_heap_size(self):
        return len(self.heap)-1

    def max_heapify(self, i):
      heap_size = self.heap_size
      l = self.left(i) #left(i)
      r = self.right(i) #right(i)
      if l <= heap_size and self.heap[l] > self.heap[i]:
        largest = l
      else:
        largest = i
      if r <= heap_size and self.heap[r] > self.heap[largest]:
        largest = r
      if i != largest:
        self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
        self.max_heapify(largest)

    def build_max_heap(self,lista):
      self.heap = lista
      self.heap_size = self.get_heap_size()
      for i in range(self.parent(self.get_heap_size()), 0, -1):
        self.max_heapify(i)

    def heap_sort(self):
        self.build_max_heap(self.heap)
        self.heap_size=self.get_heap_size()
        for i in range(self.get_heap_size(), 1, -1):
            self.heap[1], self.heap[i] = self.heap[i], self.heap[1]
            self.heap_size = self.heap_size -1
            self.max_heapify(1)

###### funciones para implementar la cola de prioridad
# #### utilizando el heap.

    def heap_maximum(self):
        return self.heap[1]

    def heap_Extract_Max(self):
        if self.heap_size<1:
            raise Exception("error")
        max= self.heap[1]
        self.heap[1],self.heap[self.heap_size]=self.heap[self.heap_size],self.heap[1]
        self.heap_size=self.heap_size-1
        self.max_heapify(1)
        return max

    def heap_increase_key(self,i,key):
        if key < self.heap[i]:
            raise Exception("Error")
        self.heap[i] = key
        while i > 1 and self.heap[i/2]< self.heap[i]:
            self.heap[i], self.heap[i/2] = self.heap[i/2], self.heap[i]
            i = i/2

    def max_heap_insert(self,key):
        self.heap_size = self.heap_size+1
        self.heap.append(key)
        return self.heap_increase_key(self.heap_size,key)

if __name__ == "__main__":

  lista = [0,4,1,3,2,16,9,10,14,8,7]

  sort= priorityQueue()
  print "Ordenar la lista con el heap sort"
  print "lista de elementos que estaran en el heap: ", lista[1:]
  # creamos el heap
  sort.build_max_heap(lista)
  sort.heap_sort()
  print  "Heap ordenado: ",sort.get_heap()
  print

  print "********COLA DE PRIORIDAD UTILIZANDO EL HEAP*******"
  lista = [0,4,1,3,2,16,9,10,14,8,7]
  print "lista de elementos que estaran en el heap: ", lista[1:]
  hp= priorityQueue()
  # creamos el heap
  hp.build_max_heap(lista)
  print  "Heap: ",hp.get_heap()
  print

  print "Valor a insertar 21"
  hp.max_heap_insert(21)
  print "Cola de prioridad con nuevo elemento: ",hp.get_heap()

  print
  print "Ver elemento maximo: ", hp.heap_maximum()
  print
  for i in range(0,hp.get_heap_size()):
      print
      print "Extraer el elemento maximo de la cola de prioridad: ",hp.heap_Extract_Max()
      print "La cola de prioridad queda asi, ",hp.get_heap()," y el heap_size es ",hp.heap_size,"."