strings = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4, 5]

# Variable array is somewhere in memory and the computer knows it.
# When I do array[2], i'm telling the computer, hey go to the array and grab the 3rd item from where the array is stored.

# Append
strings.append('e')
print(strings)
# ['a', 'b', 'c', 'd', 'e']

# Pop
strings.pop()
print(strings)
# ['a', 'b', 'c', 'd']

# Insert
strings.insert(0, 'x')
print(strings)
# ['x', 'a', 'b', 'c', 'd']

# Remove
strings.remove('b')
print(strings)
# ['x', 'a', 'c', 'd']
