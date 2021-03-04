loop, result = map(int, input().split())
data = []
count = 0

for _ in range(loop):
    data.append(int(input()))
data.sort(reverse=True)

for i in data:
    if result == 0:
        break
    if result // i > 0:
        count += result // i
        result = result % i
print(count)
