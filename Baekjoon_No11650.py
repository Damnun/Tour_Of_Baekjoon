count = int(input())
result = []
for _ in range(count):
    x = list(map(int, input().split()))
    result.append(x)
result.sort(key=lambda data: (data[0], data[1]))

for i in range(count):
    print(result[i][0], result[i][1])
