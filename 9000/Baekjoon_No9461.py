for _ in range(int(input())):
    data = int(input())
    tmp = [1, 1, 1, 1]
    dp = [0 for _ in range(data - 2)]
    dp = tmp + dp

    for i in range(4, data + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    print(dp[data])

"""
DP를 이용한 피보나치 수열의 약간변형문제
항상 식의 연계성을 생각해야 한다.
"""