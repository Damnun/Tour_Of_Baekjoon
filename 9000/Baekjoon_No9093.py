import sys
input = sys.stdin.readline

n = int(input())
a = [list(input().split()) for i in range(n)]

for i in range(n):
    for j in a[i]:
        print(''.join(reversed(list(j))), end=" ")
    print()
