count = 0

while True:
    tmp = 0
    insert = []
    value = int(input())

    if value == 0:
        break
    insert.append(tmp)

    count += 1
    tmp = 3 * value
    insert.append(tmp)

    if tmp % 2 == 0:
        tmp = tmp // 2
    elif tmp % 2 == 1:
        tmp = (tmp + 1) // 2
    insert.append(tmp)

    tmp = tmp * 3
    insert.append(tmp)

    tmp = tmp // 9
    insert.append(tmp)
    if insert[1] % 2 == 0:
        print(f'{count}. even {tmp}')
    elif insert[1] % 2 == 1:
        print(f'{count}. odd {tmp}')
