# Max-Heap
 
#             60(1)             Node -> ith index
#           /    \              left-child -> 2*i index
#         50(2)      40(3)      Right-child -> 2*i + 1 index
#        /  \                   Parent -> (i//2)
#      30(4)    20(5)
#
# [-1, 60, 50, 40, 30, 20]
#   0   1   2   3   4   5


class Heap:
    def __init__(self):
        self.arr = [-1]
        self.size = 0
    
    def insert(self, val):
        # i. Insert at end -> eg. [-1, 60, 50, 40, 30, 20, 55]
        self.size += 1
        self.arr.append(val)

        # ii. take it to its correct position -> [-1, 60, 50, 55, 30, 20, 40]
        index = self.size
        while (index > 1):
            parent = index//2
            if self.arr[parent] < self.arr[index]:
                self.arr[parent], self.arr[index] = self.arr[index], self.arr[parent]
                index = parent
            else:
                return

    def delete(self):
        if self.size == 0:
            return "Nothing to delete"

        # Step1: Put the last element into first Index
        self.arr[1] = self.arr[self.size]
        # Step2: Remove last element
        self.arr.pop()
        self.size -= 1
        
        # Step3: Take root node to its correct position
        i = 1
        while i < self.size:
            left_child = 2*i
            right_child = 2*i + 1

            if left_child < self.size and self.arr[left_child] > self.arr[i]:
                self.arr[left_child], self.arr[i] = self.arr[i], self.arr[left_child]
                i = left_child
            elif right_child < self.size and self.arr[right_child] > self.arr[i]:
                self.arr[right_child], self.arr[i] = self.arr[i], self.arr[right_child]
                i = right_child
            else:
                return
    
    def heapify(self, arr, n, i):
        largest = i
        left = 2*i
        right = 2*i+1

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)

    def print(self):
        for i in range(1, self.size+1):
            print(self.arr[i], end=" ")
        print()

heap = Heap()
heap.insert(50)
heap.insert(55)
heap.insert(53)
heap.insert(52)
heap.insert(54)
heap.print()
heap.delete()
heap.print()

arr = [-1, 54, 53, 55, 52, 50]
n = 5
for i in range(n//2,0,-1):
    heap.heapify(arr, 5, i)

print(arr)