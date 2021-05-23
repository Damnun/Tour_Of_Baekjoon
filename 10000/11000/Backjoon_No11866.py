n, k = map(int, input().split())
data = []
result = []

for i in range(n):
    data.append(i+1)

point = k - 1

while len(data) != 0:
    if len(data) <= k - 1:
        point = point % len(data)

    elif point >= len(data):
        point = point - len(data)

    result.append(data[point])
    del(data[point])
    
    point += (k - 1)

print("<", end='')
index = 0
while index < len(result):
    if index == len(result) - 1:
        print(result[index], end='>')
    else:
        print(result[index], end=', ')
    index += 1
print()