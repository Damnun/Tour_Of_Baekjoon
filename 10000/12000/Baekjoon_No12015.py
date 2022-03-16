n = int(input())
a = list(map(int, input().split()))
a = [0] + a
dp = [0]

for i in a:
    if dp[-1] < i:
        dp.append(i)
    else:
        left = 0
        right = len(dp)

        while left < right:
            mid = (left + right) // 2
            if dp[mid] < i:
                left = mid + 1
            else:
                right = mid
        dp[right] = i
print(len(dp) - 1)
print(*dp[1:])
