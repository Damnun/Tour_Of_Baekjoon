from itertools import combinations_with_replacement
n, m = map(int, input().split())
data = [i for i in range(1, n + 1)]
for i in combinations_with_replacement(data, m):
    for j in i:
        print(j, end=' ')
    print()
