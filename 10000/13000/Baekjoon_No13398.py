n = int(input())
a = list(map(int, input().split()))
d = [0] * n
d2 = [0] * n

# i번째에서 끝나는 최대 연속 합을 구해줌
for i in range(n):
    d[i] = a[i]
    if i == 0:
        continue
    if d[i] < d[i - 1] + a[i]:
        d[i] = d[i - 1] + a[i]

# i번쨰에서 시작하는 최대 연속 합을 구해줌
for i in range(n - 1, -1, -1):
    d2[i] = a[i]
    if i == (n - 1):
        continue
    if d2[i] < d2[i + 1] + a[i]:
        d2[i] = d2[i + 1] + a[i]

ans = max(d)
# i - 1번째에서 끝나는 최대 연속 합과 i + 1에서 시작하는 최대 연속 합을 더했을 때
# 그 값이 ans보다 더 크다면(i를 제거한 연속 합이 더 클 때) 그 값을 ans로 지정.
for i in range(1, n - 1):
    if ans < d[i - 1] + d2[i + 1]:
        ans = d[i - 1] + d2[i + 1]
print(ans)

"""
수열의 연속합 중 가장 큰 합을 구하는 문제
수는 하나 제거할 수 있다. (제거하지 않아도 됨)

연속합
D[i] = i번째에서 끝나는 최대 연속 합
A[i] = max(d[i - 1] + a[i], a[i])

1. a의 각각의 수를 한번씩 제거하면서 연속합을 구하는 방법
- 각 수를 제거할 때마다 dp를 수행해야하니 O(n^2)이 걸림

2. 바이토닉 부분 수열의 아이디어를 차용
- d[i] = i번째에서 끝나는 최대 연속 합
- d2[i] = i번째에서 시작하는 최대 연속합
- 즉 d[i - 1] + d2[i + 1]로 하면 i번쨰를 제거할 수 있음.
- 0번쨰와 N번째는 제거하지 않아도 됨.
"""
