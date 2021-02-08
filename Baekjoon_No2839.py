sugar = int(input())
cnt = 0
while True:
    if (sugar % 5) == 0:
        cnt += sugar//5
        print(cnt)
        break
    sugar -= 3
    cnt += 1
    if sugar < 0:
        print("-1")
        break
