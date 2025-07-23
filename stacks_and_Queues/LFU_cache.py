class Node:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)  # dummy head
        self.tail = Node(None, None)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_at_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def remove_last(self):
        if self.head.next == self.tail:
            return None  # empty
        last = self.tail.prev
        self.remove_node(last)
        return last

    def is_empty(self):
        return self.head.next == self.tail

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_table = {}     # key -> Node
        self.freq_table = {}    # freq -> DoublyLinkedList

    def get(self, key: int) -> int:
        if key not in self.key_table:
            return -1

        node = self.key_table[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_table:
            node = self.key_table[key]
            node.val = value
            self._update_freq(node)
        else:
            if len(self.key_table) >= self.capacity:
                lfu_list = self.freq_table[self.min_freq]
                removed = lfu_list.remove_last()
                if removed:
                    del self.key_table[removed.key]

            new_node = Node(key, value)
            self.key_table[key] = new_node
            if 1 not in self.freq_table:
                self.freq_table[1] = DoublyLinkedList()
            self.freq_table[1].insert_at_head(new_node)
            self.min_freq = 1

    def _update_freq(self, node):
        freq = node.freq
        self.freq_table[freq].remove_node(node)

        if self.freq_table[freq].is_empty():
            del self.freq_table[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        node.freq += 1
        if node.freq not in self.freq_table:
            self.freq_table[node.freq] = DoublyLinkedList()
        self.freq_table[node.freq].insert_at_head(node)

