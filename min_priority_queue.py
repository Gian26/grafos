__author__ = 'ING26'

class min_priorityQueue:
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
        return self.heap[1:self.heap_size+1]

    #def get_heap_size(self):
    #    return len(self.heap[1:])

    def min_heapify(self, i):
      heap_size = self.heap_size
      l = self.left(i) #left(i)
      r = self.right(i) #right(i)
      if l <= heap_size and self.heap[l] <= self.heap[i]:
        largest = l
      else:
        largest = i
      if r <= heap_size and self.heap[r] <= self.heap[largest]:
        largest = r
      if i != largest:
        self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
        self.min_heapify(largest)

    def build_min_heap(self,lista):
      self.heap = lista
      self.heap_size = len(self.heap[1:])
      for i in range(self.parent(self.heap_size), 0, -1):
        self.min_heapify(i)

    def heap_sort(self):
        self.build_min_heap(self.heap)
        self.heap_size=self.heap_size
        for i in range(self.heap_size, 1, -1):
            self.heap[1], self.heap[i] = self.heap[i], self.heap[1]
            self.heap_size = self.heap_size -1
            self.min_heapify(1)

###### funciones para implementar la cola de prioridad
# #### utilizando el heap.

    def heap_minimum(self):
        return self.heap[1]

    def heap_Extract_Minimum(self):
        if self.heap_size<1:
            raise Exception("underflow")
        mini= self.heap[1]
        self.heap[1],self.heap[self.heap_size]=self.heap[self.heap_size],self.heap[1]
        self.heap_size=self.heap_size-1
        self.min_heapify(1)
        return mini

    def heap_decrease_key(self,i,key):
        if key[0] > self.heap[i][0]:
            raise Exception("llave nueva es mas grande que el actual")
        self.heap[i]=key
        while i > 1 and self.heap[i/2] >= self.heap[i]:
            self.heap[i], self.heap[i/2] = self.heap[i/2], self.heap[i]
            i = i/2

    def min_heap_insert(self,key):
        self.heap_size = self.heap_size+1
        self.heap.append(key)
        return self.heap_decrease_key(self.heap_size,key)
