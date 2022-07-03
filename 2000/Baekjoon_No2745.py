a, b = input().split(" ")
a = ''.join(reversed(a))
b = int(b)

data = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0

for cur in range(len(a) - 1, -1, -1):
    ans += data.index(a[cur]) * (b ** cur)
print(ans)
