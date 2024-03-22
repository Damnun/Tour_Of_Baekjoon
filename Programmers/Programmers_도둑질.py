def solution(money):
    # 첫 집을 터는 경우
    dp = [0] * len(money)
    
    # 집이 1개일 경우 그 집을 터는게 최대값
    dp[0] = money[0] 
    
    # 집이 2개일 경우, 두 집 중 가장 머니가 큰 집을 터는게 최대값
    dp[1] = max(money[0], money[1])
    
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 1], money[i] + dp[i - 2])
    
    
    # 마지막 집을 터는 경우
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])
    
    return max(max(dp), max(dp2))
