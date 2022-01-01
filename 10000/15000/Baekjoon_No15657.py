n, m = map(int, input().split())
data = [0] * m
ns = list(map(int, input().split()))
ns.sort()

def go(index, start, n, m):
    if index == m:
        print(*data)
        return

    for i in range(start, n):
        data[index] = ns[i]
        go(index + 1, i, n, m)

go(0, 0, n, m)
