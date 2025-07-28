class Solution:

    def initializeHeap(self):
        self.heap = []
        

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
        

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
        return self.heap[0]
        

    def heapSize(self):
        return len(self.heap)

    def heapify_up(self,i):
        parent = (i - 1)//2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1)//2

    def heapify_down(self, i):
        size = len(self.heap)

        while True:
            smallest = i
            left_child = 2*i + 1
            right_child = 2*i + 2

            if left_child < size and self.heap[left_child] < self.heap[i]:
                smallest = left_child

            if right_child < size and self.heap[right_child] < self.heap[i]:
                smallest = right_child

            if smallest == i:
                return 
            
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

heap = Solution()

heap.initializeHeap()

heap.insert(4)
heap.insert(1)

print(heap.extractMin())
print(heap.getMin())

heap.insert(1)
print(heap.heapSize())

print(heap.isEmpty())

print(heap.extractMin())

heap.changeKey(0,2)

print(heap.heapSize())

print(heap.getMin())



