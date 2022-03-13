"""
1. n/2으로 나누어 left/right 에서 모든 부분수열의 합을 구해줌 m = n/2
2. 정렬 2^mlog2^m
3. o(2^m) > 2^mlog2^m = m2^m = n/2*2^n/2 =
"""
n, s = map(int, input().split())
a = list(map(int, input().split()))

# 이분 탐색을 위한 정렬 과정
m = n // 2
n -= m
first = [0] * (1 << n)
for i in range(1 << n):
    for k in range(n):
        if (i & (1 << k)) > 0:
            first[i] += a[k]

second = [0] * (1 << m)
for i in range(1 << m):
    for k in range(m):
        if (i & (1 << k)) > 0:
            second[i] += a[k + n]

first.sort()
second.sort(reverse=True)

n, m = (1 << n), (1 << m)
ans, i, j = 0, 0, 0

while i < n and j < m:
    # 값이 같을 때
    if first[i] + second[j] == s:
        c1, c2 = 1, 1
        i += 1
        j += 1
        # 값이 같을 때 똑같은 값이 얼마나 더 나오는지
        while i < n and first[i] == first[i - 1]:
            c1 += 1
            i += 1
        while j < m and second[j] == second[j - 1]:
            c2 += 1
            j += 1
        ans += c1 * c2 # 순서쌍 (곱의 법칙)
    # 값이 더 작으면 left(i)를 1 증가
    elif first[i] + second[j] < s:
        i += 1
    # 값이 더 크면 right(j)를 1 감소 (reverse 되어있으니 증가)
    else:
        j += 1
if s == 0:
    ans -= 1
print(ans)
