def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, x, y):
    x, y = find(p, x), find(p, y)
    if x < y:
        p[y] = x
    elif x > y:
        p[x] = y
    else:
        return


n = int(input())
p = [0] * (n + 1)

for i in range(1, n + 1):
    p[i] = i

for i in range(n - 2):
    x, y = map(int, input().split())
    union(p, x, y)

result = []
for i in range(1, n + 1):
    result.append(find(p, i))

for i in range(1, len(result)):
    if result[i - 1] != result[i]:
        if result.count(result[i - 1]) > result.count(result[i]):
            print(result[i - 1], result[i])
            break
        else:
            print(result[i], result[i - 1])
            break
