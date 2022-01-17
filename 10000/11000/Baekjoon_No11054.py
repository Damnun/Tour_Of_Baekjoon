"""
바이토닉 수열
증가하다가 어떤 기점을 중심으로 다시 감소하는 수열.
즉 i번째에서 끝나는 가장 긴 증가하는 부분수열 + i번째에서 시작하는 가장 긴 감소하는 부분수열이다.
"""

n = int(input())
a = list(map(int, input().split()))
d = [0] * n
d2 = [0] * n

# 가장 긴 증가하는 부분 수열 찾기
for i in range(n):
    d[i] = 1 # 만약 증가하지 않는다면 1로 초기화
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

# 가장 긴 감소하는 부분 수열 찾기
for i in range(n - 1, -1, -1):
    d2[i] = 1
    for j in range(i + 1, n):
        if a[i] > a[j] and d2[i] < d2[j] + 1:
            d2[i] = d2[j] + 1

result = [d[i] + d2[i] - 1 for i in range(n)]
print(max(result))
