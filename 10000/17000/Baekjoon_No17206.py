MAX = 80000
ans = 0

int(input())
a = list(map(int, input().split()))
b = [0] * (MAX + 1)

for i in range(MAX + 1):
    if i % 3 == 0 or i % 7 == 0:
        ans += i
    b[i] = ans

for i in a:
    print(b[i])
