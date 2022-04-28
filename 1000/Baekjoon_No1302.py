n = int(input())
a = []
result = []
d = dict()

for i in range(n):
    a.append(input())

for i in list(set(a)):
    d[i] = a.count(i)

for i in d.keys():
    if d[i] == max(d.values()):
        result.append(i)
result.sort()
print(result[0])
