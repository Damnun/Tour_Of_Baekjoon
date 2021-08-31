n = int(input())
data = list(map(int, input().split()))
dp = [0 for _ in range(len(data))]

for i in range(n):
    for j in range(i):
        if data[i] > data[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
print(*dp)

"""
첫번째 인덱스 부터 데이터 길이의 최대값을 저장
data[i]보다 작은 숫자 중 가장 큰 길이를 구하고
그 길이에 1을 더해주면 가장 긴 큰 수열이 나온다.
오랜만에 알고리즘 문제를 풀려고 하니 머리가 아프다.
2번의 수술도 잘 끝났고, 군생활 마지막 훈련도 끝났다.
나의 목표까지 조금 더 열심히 해보자.
"""