x = int(input())
b = []
tmp = x
index = 0

while tmp > 0:
    index += 1
    tmp -= index

for i in range(index):
    if i % 2 == 0:
        tmp = i+1
        while tmp > 0:
            b.append(tmp)
            tmp -= 1
    else:
        for j in range(i+1):
            b.append((j+1))

print(b[x-1], "/", b[-2])