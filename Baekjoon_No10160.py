MAX = int(1e9+9)
n, k = map(int, input().split())

if n >= 5:
    count = n * 2
    result = (k**n - count)
else:
    result = k**n

if result < 0:
    result += MAX

print(result % MAX)
