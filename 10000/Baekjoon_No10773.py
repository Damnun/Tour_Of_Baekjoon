loop = int(input())
data = []
for _ in range(loop):
    x = int(input())
    if x == 0:
        data.pop()
    else:
        data.append(x)
print(sum(data))
"""
입력에 0이 들어오면 그전의 수를 없었던 셈 치는 문제인데
파이썬의 list가 스택 구조인 것을 이용하여
0이 들어오면 이전 값을 pop하여 제거하였다.
"""