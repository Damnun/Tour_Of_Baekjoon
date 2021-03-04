while True:
    data = input()
    tmp = 0

    if data[0] == '0':
        break

    elif len(data) % 2 == 0:
        tmp = data[len(data)//2:]
        if data[0:len(data)//2] == tmp[::-1]:
            print("yes")
            continue

    elif len(data) % 2 == 1:
        tmp = data[len(data)//2+1:]
        if data[0:len(data)//2] == tmp[::-1]:
            print("yes")
            continue
    print("no")
