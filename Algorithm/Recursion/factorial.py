def find_factorial_recursive(n):
    if n == 2:
        return n
    return n*find_factorial_recursive(n-1)


print(find_factorial_recursive(4))


def find_factorial_iterative(n):
    for i in reversed(range(n)):
        if i == 0:
            return n
        n = n * i


print(find_factorial_iterative(4))
