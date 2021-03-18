def selection_sort(array):
    length = len(array)
    min = 0
    for i in range(length):
        for j in range(i, length - 1):
            if array[min] > array[j + 1]:
                min = j+1
        array[i], array[min] = array[min], array[i]
    return array


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selection_sort(numbers))
