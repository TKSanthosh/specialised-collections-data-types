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

# array concatenation
b = arr.array("i", [2, 4, 3, 5, 6])
c = arr.array("i")
c =a + b
print(c)

#array slicing
print(a[0:5])

#looping in array
for x in a:
    print(x)
print("slicing")
for x in a[1:6]:
    print(x)

print("\nwhile loop")
f=0
while f<len(a):
    print(a[f])
    f=f+1

