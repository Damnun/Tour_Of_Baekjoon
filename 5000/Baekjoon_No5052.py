import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [input().rstrip() for _ in range(n)]
    a.sort()

    for i in range(n - 1):
        length = len(a[i])
        if a[i] == a[i+1][:length]:
            print('NO')
            break
    else:
        print('YES')
