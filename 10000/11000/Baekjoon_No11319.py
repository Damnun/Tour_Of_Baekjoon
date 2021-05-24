mo = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
loop = int(input())

for _ in range(loop):
    data = input()
    jacount = 0
    mocount = 0

    for i in data:
        if i in mo:
            mocount += 1
        elif i == ' ':
            continue
        else:
            jacount += 1

    print(jacount, mocount)
