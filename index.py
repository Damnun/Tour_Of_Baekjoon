while True:
    x = input()
    y = input()
    x = int(x)
    y = int(y)

    if x < -1000 or x > 1000 or x != 0:
        break
    if y < -1000 or y > 1000 or y != 0:
        break

if x > 0:
    if y > 0:
        print("1")
    else:
        print("4")

else:
    if y > 0:
        print("2")
    else:
        print("3")

