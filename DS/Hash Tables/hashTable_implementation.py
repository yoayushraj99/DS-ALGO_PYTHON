class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
            self.data[address].append([key, value])
        else:
            self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        if self.data[address]:
            for i in self.data[address]:
                if i[0] == key:
                    return i[1]
        return None


new_hash = HashTable(4)
print(new_hash)
# {'size': 4, 'data': [None, None, None, None]}

new_hash.set('apples', 100)
new_hash.set('bananas', 20000)
print(new_hash)
# {'size': 4, 'data': [None, None, None, [['apples', 100], ['bananas', 20000]]]}

print(new_hash.get('apples'))
# 100

