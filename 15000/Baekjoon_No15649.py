from itertools import permutations
tmp, m = map(int, input().split())
n = []
for i in range(tmp):
    n.append(i+1)
permute = permutations(n,m)
for i in list(permute):
    for j in i:
        print(j,"", end='')
    print()