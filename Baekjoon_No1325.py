n, m = map(int, input().split())
relation = [[] for _ in range(n + 1)]

for _ in range(m):
    one, two = map(int, input().split())
    relation[two].append(one)

for i in range(1, m):
    for j in relation[i]:
        relation[i] = relation[i] + relation[j]

result = []
for i in range(1, m):
    result.append((i, len(relation[i])))
result = sorted(result, key = lambda x: x[1], reverse=True)

for i in range(len(result) - 1):
    print(result[i][0], end=' ')
    if result[i+1][1] != result[i][1]:
        break
print(relation)