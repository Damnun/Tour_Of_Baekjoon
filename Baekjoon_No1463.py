a = int(input())
count = 0
while a != 0:
    if (a-1) / 9 >= 1 and (a-1) % 9 == 0:
        a -= 1
        count += 1

    elif (a-1) / 4 >= 1 and (a-1) % 4 == 0:
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
