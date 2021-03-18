# In Bubble Sort we just have to check the that the item next to your current item is lesser or not.
# if it's lesser than the current item then swap it with the current item.
# Do this till we set the greatest item to the end of the array.
# After this decrease the checking length of the array because we already set the greatest item of the array to the end.

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
