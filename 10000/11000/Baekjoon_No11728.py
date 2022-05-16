import sys
input = sys.stdin.readline

a, b = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))


z = x + y
ans = ' '.join(map(str, sorted(z)))
print(ans)
