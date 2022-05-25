from math import factorial
n, k = map(int, input().split())
res = factorial(n) // (factorial(n - k) * factorial(k))
print(res % 10007)
