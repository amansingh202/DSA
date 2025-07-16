class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.MAX
    
    #add key value pair
    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
    

t = HashTable()
# t.add('march 6', 130)
# t.add('march 17', 459)
# t.add('march 20', 234)
# print(t.get_hash('march 6'))
# print(t.get_hash('march 17'))
# print(t.get('march 6'))
# t['march 6'] = 141
# print(t['march 6'])
# del t['march 9']
# print(t.arr)
t['march 6'] = 120
t['march 6'] = 78
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459
t['march 31'] = 678
# print(t.get_hash('march 6'))
# print(t.get_hash('march 17'))
# print(t['march 6']) #value overridden due to collision
print(t.arr)
del t['march 31']
print(t.arr)