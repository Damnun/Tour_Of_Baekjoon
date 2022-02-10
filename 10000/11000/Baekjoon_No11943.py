a, b = map(int, input().split())
c, d = map(int, input().split())

ans = min((a + d), (b + c))
print(ans)
