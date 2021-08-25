from collections import ChainMap

a ={1: "hello", 2:"hi"}
b ={3: "hmm" , 4:"kk"}
al =ChainMap(a,b)
print(al)