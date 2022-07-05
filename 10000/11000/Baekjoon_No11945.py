n, m = map(int, input().split(' '))
a = []
for i in range(n):
    a.append(input())
for j in a:
    print(j[::-1])
