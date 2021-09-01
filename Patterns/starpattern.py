n = int(input())
k = 2 * n - 2
for a in range(0, n + 1):
    for b in range(0, k):
        print(end=" ")
    k = k - 1
    for b in range(1, a + 1):
        print("*", end=" ")
    print("\r")
