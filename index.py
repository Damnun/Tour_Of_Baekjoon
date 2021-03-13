from math import gcd
loop = int(input())
for _ in range(loop):
    x, y  = map(int, input().split())
    result = x*y // gcd(x, y)
    print(result)