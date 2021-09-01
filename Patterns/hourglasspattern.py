def pattern(n):
    k = n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ", end="")
        print('\r')
    for a in range(0, n + 1):
        for b in range(0, k):
            print(end=" ")
        k = k - 1
        for b in range(1, a + 1):
            print("*", end=" ")
        print("\r")


pattern(5)
