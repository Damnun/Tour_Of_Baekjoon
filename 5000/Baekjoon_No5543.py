data = []
for _ in range(5):
    tmp = int(input())
    data.append(tmp)

print(min(data[0:3]) + min(data[3:]) - 50)
