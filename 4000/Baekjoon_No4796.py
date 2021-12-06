count = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    result = (v // p) * l
    if v - (v // p) * p < l:
        result += v - (v // p) * p
    else:
        result += l

    print("Case %d:" %count, result)
    count += 1
