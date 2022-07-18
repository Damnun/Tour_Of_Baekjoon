n = int(input())
v = list(map(int, input().split(' ')))
ans = max(v)
print(sum(v) - ans)
