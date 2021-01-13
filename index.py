def cal(x):
    if x >= 0 and x < 10:
        x *= 10
    x = (x / 10) + (x % 10)
    return int(x)


tmp = index = num = int(input())
cnt = 0

while True:
    num = cal(tmp)
    tmp = ((tmp % 10) * 10) + (num % 10)
    cnt += 1
    if tmp == index:
        print(cnt)
        break
