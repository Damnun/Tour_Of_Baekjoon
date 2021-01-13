a = 0
b = []

while a != 9:
    num = int(input())
    b.append(num)
    a += 1

print(max(b))
print(b.index(max(b))+1)