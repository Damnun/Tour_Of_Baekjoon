n = input()
f = int(input())

ans = int(n[:-2] + '00')
while True:
    if ans % f == 0:
        break
    ans += 1
print(str(ans)[-2:])
