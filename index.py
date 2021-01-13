a = int(input())
b = int(input())
c = int(input())

result = a*b*c
a = []

for i in str(result):
    a.append(int(i))

for i in range(10):
    print(a.count(i))
