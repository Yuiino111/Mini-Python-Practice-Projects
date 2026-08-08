class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(c) for c in string)
    
    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {}
        self.collection[hash_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
            if not self.collection[hash_key]:
                del self.collection[hash_key]

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        return None

#Test
print(HashTable().hash('golf'))
