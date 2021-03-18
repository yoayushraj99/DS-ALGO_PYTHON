def bubble_sort(array):
    length = len(array)

    for i in range(length):
        for j in range(length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(bubble_sort(numbers))
# [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
