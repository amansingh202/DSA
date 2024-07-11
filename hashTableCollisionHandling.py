#collision handling in hash table

'''Collision means when there is same index values for different keys suppose march 6 and march 17 have the index values then it is a case of collision
In this cdde we will look at that how we can handle collisions in our program. As in the code hashTable.py we have seen that we can calculate the index values 
based on the ASCII characters and then divide the result by 100 and the remaining modulus will provide the index value for that particular key where a value can 
be stored'''

'''
1. chaining can be used to overcome the case of collision as in case if two keys have the same index value then we can use a link list or a chain to append that 
storage 

2. linear probing: in case of collision we go to the next available location in the prev or the next direction

'''

class HashTable:

    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]

    def get_hash(self, key):
        h = 0

        for char in key:
            h += ord(char)

        return h % self.max
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False

        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def __delitem__ (self, key):
        h = self.get_hash(key)

        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
    

t = HashTable()

#both march 6 and march 17 have same ascii values
print(t.get_hash("march 6"))
print(t.get_hash("march 17"))

t['march 6'] = 120
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459


#here as march 6 and march 17 have the same index values so march 17 have overwrote the value for march 6
print(t['march 6'])

#to overcome make changes in the setitem method and the arr
print(t.arr)
print(t['march 17'])

del t['march 17']
print(t.arr)
