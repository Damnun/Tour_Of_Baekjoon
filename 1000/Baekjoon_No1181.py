count = int(input())
result = []
for _ in range(count):
    data = input()
    if data not in result:
        result.append(data)
result.sort(key=lambda x: (len(x), x))

for i in result:
    print(i)
