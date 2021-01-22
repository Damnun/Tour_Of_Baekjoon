x = int(input())
tmp = x
result = 0
index = 0
a = []
b = []

while tmp > 0:
    index += 1
    tmp -= index

for i in range(index):
    b.append(i+1)

a = b[::-1]
result = tmp + index - 1

if index % 2 == 0:
    print(b[result], "/", a[result])
else:
    print(a[result], "/", b[result])
