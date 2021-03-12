def fibonacci_iterative(n):
    array = [0, 1]
    for i in range(2, n + 1):
        array.append(array[-1] + array[-2])
    return array[n]


print(fibonacci_iterative(8))


def fibonacci_recursive(n):
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(5))
