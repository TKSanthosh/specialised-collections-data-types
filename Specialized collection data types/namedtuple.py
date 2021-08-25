from collections import namedtuple

a = namedtuple('courses', 'name, date')
s = a('datascience', 'hello')
print(s)
#namedtuple using list
d= a._make(['hello','hi'])
print(d)