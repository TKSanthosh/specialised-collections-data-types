from collections import Counter

a= [1,2,3,2,1,2,2,1,4,2,4,1]
c = Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub= {2:1 , 1:2}
c.subtract(sub)
print(c.most_common())
