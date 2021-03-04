while True:
    data = list(map(int, input().split()))
    data.sort()
    if sum(data) == 0:
        break
    else:
        if data[2]**2 == data[0]**2 + data[1]**2:
            print("right")
        else:
            print("wrong")