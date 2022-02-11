n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()


def solution(array, target, s, e):
    while s <= e:
        m = (s + e) // 2

        if array[m] == target:
            return m
        elif array[m] > target:
            e = m - 1
        else:
            s = m + 1
    return


for i in range(m):
    if solution(a, b[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
