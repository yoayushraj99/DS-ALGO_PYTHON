array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]


# Method-1

def merge_sorted_arrays1(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    merged_array = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    return merged_array + arr1[i:] + arr2[j:]


print(merge_sorted_arrays1(array1, array2))


# [0, 3, 4, 4, 6, 30, 31]


# Method-2

def merge_sorted_arrays2(arr1, arr2):
    merged_array = arr1 + arr2
    merged_array.sort()
    return merged_array


print(merge_sorted_arrays2(array1, array2))
# [0, 3, 4, 4, 6, 30, 31]
