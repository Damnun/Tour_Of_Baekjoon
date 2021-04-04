n = int(input())
data = [float(input()) for _ in range(n)]
for i in range(1, n):
    data[i] = max(data[i], data[i] * data[i - 1])
print("%.3f" % (max(data)))

"""
DP를 이용하여 연속값중 최댓값을 구하는 문제
배열을 1씩 증가시키면서
현재 값이 더 큰지, 아니면 지금까지의 곱 값이 더 큰지를  max 함수로구별하여
다시 데이터에 넣어준다.
"""
