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

    def keys(self):
        keys = []
        for i in self.data:
            if i is not None:
                keys.append(i[0][0])
        return keys

    def values(self):
        values= []
        for i in self.data:
            if i is not None:
                values.append(i[0][1])
        return values


new_hash = HashTable(5)
print(new_hash)
# {'size': 5, 'data': [None, None, None, None, None]}

new_hash.set('apples', 100)
new_hash.set('bananas', 20000)
print(new_hash)
# {'size': 5, 'data': [None, None, None, [['bananas', 20000]], [['apples', 100]]]}

print(new_hash.get('apples'))
# 100

print(new_hash.keys())
# ['bananas', 'apples']

print(new_hash.values())
# [20000, 100]

