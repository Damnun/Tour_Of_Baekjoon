"""
모든 부분 수열의 개수 = 2^n - 1개 (공집합 제외)
전체 집합 = (1 << N) - 1
1182번을 combinations이 아닌 비트 마스크를 이용해 풀이해보았다.
"""
n, s = map(int, input().split())
a = list(map(int, input().split()))
result = 0
for i in range(1, (1<<n)):
    ans = 0
    # 합 계산, i = 비트마스크
    for j in range(n):
        if (i & (1 << j)):
            ans += a[j]

    if ans == s:
        result += 1
print(result)
