a = int(input())
index = 1
stack = 1

if a == 1:
    print(1)

else:
    while True:
        stack += (6*index)
        index += 1
        if a <= stack:
            print(index)
            break
