n, m = map(int, input().split())
data = [0] * m
check = [False] * (n + 1)
ns = list(map(int, input().split()))
ns.sort()

def go(index, start, n, m):
    if index == m:
        print(*data)
        return

    for i in range(start, n):
        if check[i]:
            continue
        check[i] = True
        data[index] = ns[i]
        go(index + 1, 0, n, m)
        check[i] = False

go(0, 0, n, m)
