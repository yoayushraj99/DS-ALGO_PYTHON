def merge_sort(array):
    length = len(array)
    if length == 1:
        return array
    left = array[:int(length / 2)]
    right = array[int(length / 2):]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    merged_array = []
    return merge(left)


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(merge_sort(numbers))
