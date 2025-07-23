class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_at_front(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_at_front(node)
        else:
            new_node = Node(key, value)
            self._insert_at_front(new_node)
            self.cache[key] = new_node

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)#; // cache is {1=1, 2=2}
print(lRUCache.get(1))#;    // return 1
lRUCache.put(3, 3)#; // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))#;    // returns -1 (not found)
lRUCache.put(4, 4)#; // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))#;    // return -1 (not found)
print(lRUCache.get(3))#;    // return 3
print(lRUCache.get(4))#;    // return 4