k, l = map(int, input().split())

ans = False
for i in range(2, l):
    if k % i == 0:
        print("BAD", i)
        ans = True
        break

if not ans:
    print("GOOD")
