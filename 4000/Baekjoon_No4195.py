def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, a, b):
    a = find(p, a)
    b = find(p, b)

    if a != b:
        p[b] = a
        number[a] += number[b]


for _ in range(int(input())):
    p = dict()
    number = dict()
    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')
        if x not in p:
            p[x] = x
            number[x] = 1
        if y not in p:
            p[y] = y
            number[y] = 1

        union(p, x, y)
        print(number[find(p, x)])
