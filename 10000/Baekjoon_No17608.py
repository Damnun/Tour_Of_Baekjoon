data = []
result = 1
count = int(input())
if count <= 0:
    exit()

for _ in range(count):
    data.append(int(input()))

tmp = data.pop()
for _ in range(count - 1):
    index = data.pop()
    if index > tmp:
        tmp = index
        result += 1
print(result)
