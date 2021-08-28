n =  int(input("Enter the factorial no:"))
a=1
if n != 0:
    for x in range (1,n+1):
        a=a*x
    print(a)
else:
    print("Factorial is One")
