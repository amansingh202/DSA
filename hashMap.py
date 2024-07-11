class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

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
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    

t = HashTable()
t.add('march 6', 130)
print(t.get_hash('march 9'))
print(t.get('march 6'))
t['march 6'] = 141
print(t['march 6'])
del t['march 9']
print(t.arr)