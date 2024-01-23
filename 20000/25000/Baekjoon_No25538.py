a, b, c, d = map(int, input().split())
n = int(input())
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    fx = max(a * (y - b) ** 2 + c, d)
    if fx != x or b > y:
        continue
    result += 1

print(result)
