from collections import deque

a = [1,2,3,4,5,6]
d= deque(a)
print(d)
d.appendleft("hello")
print(d)

d.pop()
print(d)