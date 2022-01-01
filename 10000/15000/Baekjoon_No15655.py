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
        go(index + 1, i + 1, n, m)
        check[i] = False

go(0, 0, n, m)
"""
주어진 수 N개의 리스트에서 중복 없이 오름차순으로 m개를 뽑는 방법의 수를
재귀를 통해 나타낸다.
check를 통해 선택된 수 / 선택되지 않은 수를 구별하고, 인덱스를 1씩 늘려주면서
1,6 6,1 같은 중복수가 나오지 않게 한다.
"""
