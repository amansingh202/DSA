class Solution:

    def initializeHeap(self):
        self.heap = []
        

    def insert(self, key):
        self.heap.append(key)
        self.heap.heapify_up(len(self.heap) - 1)
        

    def changeKey(self, index, new_val):
        if index < 0 or index > len(self.heap):
            return
        old_val = self.heap[index]
        self.heap[index] = new_val

        if new_val < old_val:
            self.heapify_up(index)
        else:
            self.heapify_down(index)
        

    def extractMin(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return root
        

    def isEmpty(self):
        return len(self.heap) == 0
        

    def getMin(self):
        

    def heapSize(self):
        return len(self.heap)

    def heapify_up(self,i):
        pass

    def heapify_down(self, i):
        pass
        