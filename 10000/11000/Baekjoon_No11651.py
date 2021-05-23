loop = int(input())
result = []
for _ in range(loop):
    data = list(map(int, input().split()))
    result.append(data)

result.sort(key=lambda x: (x[1], x[0]))
for i in result:
    print(i[0], i[1])
