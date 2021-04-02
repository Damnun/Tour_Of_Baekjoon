n = int(input())
data = [0 for _ in range(n + 1)]

data[1] = 1

if n >= 2:
    data[2] = 2

for i in range(3, n + 1):
    data[i] = data[i - 1] + data[i - 2]
    data[i] %= 15746
print(data[n])

"""
문제를 확률과 통계처럼 꾸며놨을 뿐
사실상 근본은 피보나치와 같다.
"""