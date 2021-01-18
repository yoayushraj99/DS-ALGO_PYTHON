class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def index(self, index):
        return self.data[index]

    def append(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.data

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete_at_index(self, index):
        item = self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


myArray = MyArray()

myArray.append('hi')
# {'length': 1, 'data': {0: 'hi'}}

myArray.append('you')
# {'length': 2, 'data': {0: 'hi', 1: 'you'}}

myArray.append('!')
# {'length': 3, 'data': {0: 'hi', 1: 'you', 2: '!'}}

myArray.pop()
# {'length': 2, 'data': {0: 'hi', 1: 'you'}}

myArray.delete_at_index(0)
# {'length': 1, 'data': {0: 'you'}}

myArray.append('are')
# {'length': 2, 'data': {0: 'you', 1: 'are'}}

myArray.append('nice')
# {'length': 3, 'data': {0: 'you', 1: 'are', 2: 'nice'}}

myArray.shift_items(0)

print(myArray)
# {'length': 2, 'data': {0: 'are', 1: 'nice'}}
