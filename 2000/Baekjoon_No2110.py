import sys
input = sys.stdin.readline
n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

start, end = 1, (a[-1] - a[0])
answer = 0

while start <= end:
    mid = (start + end) // 2
    cur = a[0]
    count = 1

    for i in range(1, len(a)):
        if a[i] >= cur + mid:
            count += 1
            cur = a[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
