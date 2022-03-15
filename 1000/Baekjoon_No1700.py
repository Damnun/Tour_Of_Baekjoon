from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
plugs = []

while a:
    x = a.pop(0)
    if x in plugs:
        continue

    pri = Counter(a)
    plugs.append(x)

    if len(plugs) > n:
        minimum = []
        for j in range(n):
            if plugs[j] in a:
                minimum.append((pri[plugs[j]], a.index(plugs[j]), j))
            else:
                minimum.append((pri[plugs[j]], float('inf'), j))

        minimum = sorted(minimum, key=lambda v: (v[1], v[0]))
        del plugs[minimum[-1][2]]
        count += 1
print(count)
