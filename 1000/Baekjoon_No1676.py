data = int(input())
if data == 0:
    print("0")
    exit()

dp = [0 for _ in range(data + 1)]
dp[0], dp[1] = 0, 1

for i in range(2, data + 1):
    dp[i] = i * dp[i - 1]


result = str(dp[data])
index = len(result) - 1
count = 0
while True:
    if result[index] == '0':
        count += 1
    elif result[index] != '0' or index == -1:
        print(count)
        break
    index -= 1

"""
DP를 이용해 팩토리얼을 구현하였고, 구현한 값을 str로 변환하여 리버스 인덱싱을 통해 문제를 해결하였다.
"""