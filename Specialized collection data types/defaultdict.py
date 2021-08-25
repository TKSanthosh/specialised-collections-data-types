from collections import defaultdict

d= defaultdict(int)
d[1]="san"
d[2]="tho"
d[3] = "sh"
print(d)
print(d[4])
a={1:"san", 2:"tho", 3:"sh"}
print(a[4]) #it will show error - keyError: 4 this is how it differs from defaultdict