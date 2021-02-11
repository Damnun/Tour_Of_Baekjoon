import math
ans = int(input())
for i in range(ans):
    arr = [1]
    tmp = 2
    a, b = map(int, input().split())
    if (b-a) <= 3:
        print(b-a)
    else:
        n = int(math.sqrt(b-a))
        if b-a == n ** 2:
            print(2*n-1)
        elif n ** 2 < b-a <= n ** 2 + n:
            print(2*n)
        else:
            print(2*n+1)

