a = int(input())
count = 0

while a != 1:

    if (a-1) % 9 == 0 or (a-1) % 4 == 0:
        a -= 1
        count += 1

    if a % 3 == 0 and (a / 3) >= (a / 2):
        a = a//3
        count += 1

    elif a % 2 == 0 and (a / 2) >= (a / 3):
        a = a//2
        count += 1


print(count)


# 중복값 제거 및 2중연산 고려해야함
# 다이나믹 프로그래밍
