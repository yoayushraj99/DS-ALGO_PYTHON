def insertion_sort(array):
    length = len(array)

    for i in range(length-1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            if i >= 1:
                for j in range(i, 0, -1):
                    if array[j] < array[j-1]:
                        array[j], array[j-1] = array[j-1], array[j]
    return array


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(insertion_sort(numbers))
# [2,44,6,99,1]
