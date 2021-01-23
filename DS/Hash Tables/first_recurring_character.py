def fast_first_recurring_character(array):
    table = {}
    for item in array:
        if item in table:
            return item
        else:
            table[item] = True
    return None


print(fast_first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]))
# 2


def naive_first_recurring_character(array):
    for item1 in range(len(array)):
        for item2 in range(1, len(array)):
            if array[item1] == array[item2]:
                return array[item1]
                break
            else:
                continue
    return None


print(naive_first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]))
# 2
