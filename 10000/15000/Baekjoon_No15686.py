from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
store = []
house = []
result = 1e9

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append([i, j])
        elif maps[i][j] == 2:
            store.append([i, j])


for i in combinations(store, m):
    tmp = 0
    for j in house:
        cur = 1e9
        for k in range(m):
            cur = min(cur, abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]))
        tmp += cur
    result = min(result, tmp)

print(result)
