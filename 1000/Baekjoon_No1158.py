count, num = map(int, input().split())
a = [i for i in range(1, count + 1)]

ans = []
tmp = num - 1
while len(a):
    if tmp >= len(a):
        tmp = tmp % len(a)
    else:
        ans.append(str(a.pop(tmp)))
        tmp += (num - 1)
print("<", ", ".join(ans), ">", sep='')
