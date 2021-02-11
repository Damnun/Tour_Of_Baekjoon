n, m = map(int, input().split())
result = n-m
if result < 0: 
    result *= -1
print(result)