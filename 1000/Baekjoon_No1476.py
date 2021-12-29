e, s, m = map(int, input().split())
data = [[1]]
count = 1
a = b = c = 1
while count <= 7980:
    if a == 16:
        a = 1
    if b == 29:
        b = 1
    if c == 20:
        c = 1

    data.append([a, b, c])

    a += 1
    b += 1
    c += 1
    count += 1
print(data.index([e, s, m]))
