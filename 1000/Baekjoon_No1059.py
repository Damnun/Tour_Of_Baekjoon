import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.append(0)
a.sort()
target = int(input())

ans = 0
for i in range(len(a) - 1) :
    if a[i] == target or a[i + 1] == target:
        ans = 0
        break
    elif a[i] < target < a[i + 1]:
        ans = (target - a[i]) * (a[i + 1] - target) - 1
        break

print(ans)
