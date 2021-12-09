n = int(input())
data = list(int(input()) for _ in range(n))
data.sort()

result = 0
while True:
    if len(data) == 0:
        break
    elif len(data) == 1:
        result += data.pop(0)
        break
    elif data[0] == 0 and len(data) >= 2:
        result += data.pop(0) + data.pop(0)
    elif data[0] < 0 and len(data) >= 2:
        tmp1 = data.pop(0)
        tmp2 = data.pop(0)
        if tmp2 < 0:
            result += tmp1 * tmp2
        elif tmp2 > 0 and (len(data) + 2) % 2 == 0:
            result += tmp1 + tmp2
        elif tmp2 > 0 and (len(data) + 2) % 2 == 1:
            data.insert(0, tmp2)
            data.insert(0, tmp1)
            tmp1 = data.pop()
            tmp2 = data.pop()
            result += tmp1 * tmp2

    elif len(data) >= 2:
        tmp1 = data.pop()
        tmp2 = data.pop()
        if tmp1 == tmp2 == 1:
            result += tmp1 + tmp2
        elif tmp1 == 1 or tmp2 == 1:
            result += tmp1 + tmp2
        else:
            result += tmp1 * tmp2
print(result)

