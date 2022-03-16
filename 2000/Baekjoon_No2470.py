n = int(input())
a = list(map(int, input().split()))
a.sort()

left, right = 0, n - 1  # 투 포인터
ans = float('inf')
answer = []

while left < right:
    l, r = a[left], a[right]
    sum = l + r
    if abs(sum) < ans:
        ans = abs(sum)
        answer = [l, r]
    if sum < 0:
        left += 1
    else:
        right -= 1
print(*answer)

