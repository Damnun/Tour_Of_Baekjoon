n, k = map(int, input().split())
a = []
a.append(n-(k-1))
for i in range(k-1):
    a.append(1)
print(a)