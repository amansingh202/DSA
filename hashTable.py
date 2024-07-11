#hashtable and hashmaping using python

def get_hash(key):
    h = 0

    for char in key:
        h += ord(char)

    return h % 100

index_value = get_hash('march 28')
#print(f"Index value is {index_value}")



#creating a hash table
#working of a dictionary
class HashTable:

    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0

        for char in key:
            h += ord(char)

        return h % self.max
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

    
t = HashTable()
t['march 6'] = 130
t['march 8'] = 20
t['march 9'] = 31

print("March 6 index value is",get_hash('march 6'))
print("March 8 index value is",get_hash('march 8'))
print("March 9 index value is",get_hash('march 9'))

#print(t.arr)

#deletes the value for the key march 6 from the array
del t['march 6']
print(t.arr)


print(t['march 6'])