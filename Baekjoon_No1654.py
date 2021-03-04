import sys

k, n = map(int, sys.stdin.readline().split())
data = []
result = 0
for _ in range(k):
    data.append(int(sys.stdin.readline()))

data_min = 1
data_max = sum(data)//n

while data_min <= data_max:
    mid = (data_max + data_min) // 2
    count = sum([x//mid for x in data])
    if count < n:
        data_max = mid - 1
    elif count >= n:
        data_min = mid + 1
        answer = mid
print(answer)

"""
이분탐색을 이용하여 풀 수 있는 문제
이분탐색에 대해서 더 공부해보자
"""