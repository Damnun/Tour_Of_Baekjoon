exe_index = 0
exe_num = int(input())
while exe_index < exe_num:
    a = int(input())
    b = int(input())
    z = []
    x = []

    for i in range(b):
        x.append(i+1)
    z.append(x)
    x = []

    for i in range(a):
        for j in range(b):
            x.append(sum(z[i][0:j+1]))
        z.append(x)
        x = []
    print(z[a][b-1])
    exe_index += 1
