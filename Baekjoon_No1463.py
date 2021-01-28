a = int(input())
count = 0

while a != 0:
    if a / 9 >= 1 or a / 4 >= 1:
        a -= 1
        count += 1

    elif a % 3 == 0:
        a /= 3
        count += 1

    elif a % 2 == 0:
        a /= 2
        count += 1

    else:
        a -= 1
        count += 1

print(count)


# 중복값 제거 및 2중연산 고려해야함
