a = int(input())
b = input().split()
c = []
for i in b:
    c.append(int(i))
del(b)

c.sort()
print(c[0], c[a-1])

