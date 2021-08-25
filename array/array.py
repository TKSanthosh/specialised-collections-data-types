import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])

# accessing the elements in array
print(a[2])

# finding the length of the array
print(len(a))

# adding elements in array using different methods
a.append(6)
print(a)
a.insert(6, 9)
print(a)
a.extend([7, 8, 10])
print(a)

# removing elements in array using different methods
print(a.pop())
print(a.pop(2))  # pop function returns the value which get popped from array

a.remove(5)  # but in remove function it wont return the value which gets removed from the array
print(a)


