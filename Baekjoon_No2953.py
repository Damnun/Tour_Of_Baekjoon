a = []
v = 0
w = 0
for i in range(5):
    a.append(list(map(int, input().split())))
    if v < sum(a[i]):
        w = i + 1
        v = sum(a[i])
print(w, v)
