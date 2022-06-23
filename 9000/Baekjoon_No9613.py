import sys
import math
input = sys.stdin.readline

for i in range(int(input())):
    a = list(map(int, input().split()))
    ans = 0
    for j in range(1, len(a)):
        for k in range(j + 1,len(a)):
            ans += math.gcd(a[j], a[k])

    print(ans)
