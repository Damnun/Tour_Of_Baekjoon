count = int(input())
result = []
for _ in range(count):
    result.append(list(input().split()))

result.sort(key=lambda x: int(x[0]))
for i in range(count):
    print(result[i][0], result[i][1])
