import sys
input = sys.stdin.readline

MAX = 5
a = list(map(int, input().split()))
n = min(a)

while True:
    cur = 0
    for i in range(MAX):
        if n % a[i] == 0:
            cur += 1
    if cur > 2:
        print(n)
        break
    n += 1
