class hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for i in range(size)]
    
    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hash_function(key)
        self.table[index].append((key,value))
    
    def get(self,key):
        index = self.hash_function(key)
        for i in self.table[index]:
            if i[0] == key:
                return i[1]
        return "not found"
    
    def display(self):
        for i,j in enumerate(self.table):
            print(f"{i} : {j}")

ht = hashtable(5)
ht.insert(2,3)
ht.insert(4,5)
ht.insert(6,7)
ht.insert(8,9)
ht.insert(8,15)
ht.display()