class HashTable:
    def __init__(self):
        self.MAX = 10
        self.data = [None for i in range(self.MAX)]

    def gethash(self, key):
        hash_val = 0
        for char in key:
            hash_val += ord(char)
        return hash_val % self.MAX
    
    def get_probe_range(self, index):
        return [*range(index, len(self.data))] + [*range(0, index)]
    
    def __getitem__(self, key):
        h = self.gethash(key)
        prob_range = self.get_probe_range(h)
        
        for prob_index in prob_range:
            element = self.data[prob_index]
            if element is None:
                return None
            if element[0] == key:
                return element[1]
        return None
            
    def __setitem__(self, key, val):
        h = self.gethash(key)
        
        if self.data[h] is None:
            self.data[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.data[new_h] = (key, val)
        print(self.data)  # Print for debugging
    
    def find_slot(self, key, index):
        prob_range = self.get_probe_range(index)
        
        for prob_index in prob_range:
            if self.data[prob_index] is None:
                return prob_index
            if self.data[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
    
    def __delitem__(self, key):
        h = self.gethash(key)
        prob_range = self.get_probe_range(h)
        
        for prob_index in prob_range:
            if self.data[prob_index] is None:
                return
            if self.data[prob_index][0] == key:
                self.data[prob_index] = None
                return  # Added return to stop further iterations if deletion successful
        print(self.data)  # Print for debugging

# Probing test
print([*range(5, 8)] + [*range(0, 5)])

# Usage example
t = HashTable()
t['March 16'] = 231
t['March 10'] = 300
t['March 12'] = 324
t['March 13'] = 366
t['March 17'] = 405
t['March 22'] = 467
t['March 29'] = 789

del t['March 10']
print(t['March 10'])  #none means element has been deleted
print(t['March 16'])