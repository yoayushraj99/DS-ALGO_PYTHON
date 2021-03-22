def binary_search(array, start, end, element):
    while start <= end:
        mid = start + (end - start) // 2
        # returns the index of the element
        if array[mid] == element:
            return mid
        # ignore the left elements if mid element is less than the element
        elif array[mid] < element:
            start = mid + 1
        # ignore right elements if mid element is greater than the element
        elif array[mid] > element:
            start = mid - 1
    # return when element is not found in the array
    return "Element Not found"


sorted_array = [1, 4, 8, 10, 13, 15]
print(binary_search(sorted_array, 0, len(sorted_array) - 1, 15))

# 5
