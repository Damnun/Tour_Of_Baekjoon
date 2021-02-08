a, b = map(int, input().split())
cnt = 0
tmp = 0
c = [-1, 0, 1]

while a != b:
    print(a, b)
    print(c[::-1], tmp)
    for i in c[::-1]:
        if a + (i + tmp) == b:
            cnt += 1
            a += (i + tmp)
            break

        elif a + (i + tmp) <= b:
            cnt += 1
            a += (i + tmp)
            break
    tmp += 1

print(cnt)



""""a, b = map(int, input().split())
b = b - a
a = 0
cnt = 1
tmp = 0
c = [0, 1, 2]

while b > 0:
    print(a, b)
    print(c[::-1], tmp)
    for i in c[::-1]:
        if b - (i + tmp) == 0:
            cnt += 1
            b -= (i + tmp)
            break

        elif b - (i + tmp) >= 0:
            cnt += 1
            b -= (i + tmp)
            break
    tmp += 1

print(cnt)
"""
