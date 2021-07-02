import sys
input = sys.stdin.readline


def solve(stair, n):
    dp = []
    dp.append(stair[0])
    for i in range(1, 3):
        if i == 1:
            dp.append(max(dp[i-1] + stair[i], stair[i]))
            continue
        dp.append(max(dp[i-2] + stair[i], stair[i-1] + stair[i]))

    for i in range(3, n):
        dp.append(max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2]))
    print(dp[-1])


stair = []
n = int(input().strip())
for i in range(n):
    stair.append(int(input().strip()))

# 3 이하의 수의 디버깅을 위한 장치
if n < 3:
    if n == 0:
        print("0")
    elif n == 1:
        print(stair[0])
    else:
        print(sum(stair))
    exit()

solve(stair, n)

"""
PS에는 정말 문제를 푸는 다양한 시각이 필요한 것 같다.
계단을 오르는게 아닌, 정상에 올라서 어떻게 올라왔어야 최대를 가져야 할 수 있는지를
생각한다면 바로 풀리는 문제였다.
전칸에서 올라온 경우의 최대값, 전전칸에서 올라온 경우의 최대값 중에서 더 큰값을 고르면
그게 N칸에서의 최대 값이 된다.
DP 문제"""