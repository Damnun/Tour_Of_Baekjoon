index = 0
exenum = int(input())

while index < exenum:
    h, w, n = map(int, input().split())
    a = []
    b = []

    for i in range(h):
        for j in range(w):
            b.append(((i+1)*100)+(j+1))
        a.append(b)
        b = []

    result_count = 0
    for i in range(w):
        for j in range(h):
            result_count += 1
            if result_count == n:
                print(a[j][i])
                break
    index += 1
