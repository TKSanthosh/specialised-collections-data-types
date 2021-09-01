from collections import OrderedDict

d= OrderedDict()
d[1]= 's'
d[2]= 'a'
d[3]= 'n'
d[1] = 'a'
print(d)
print(d.keys())
print(d.values())
d[1]= 'p'
print(d)