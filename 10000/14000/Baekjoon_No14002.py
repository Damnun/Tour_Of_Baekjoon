"""
LIS를 구하여 출력하는 문제
"""

n = int(input())
a = list(map(int, input().split()))
d = [0] * n
v = [-1] * n # a[i] 앞에 와야 하는 수의 인덱스 ( a[i] 앞에는 a[v[i]]가 와야 길이가 가장 긴 수열이됨 )

for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[j] < a[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
            v[i] = j
ans = max(d)
p = [i for i, x in enumerate(d) if x == ans][0] # LIS의 제일 마지막 값(최댓값)의 인덱스를 구해줌
print(ans)
print(v)

def go(p): # 제일 마지막 값을 기준으로 v[p] 값을 이어나가며 출력해줌 (재귀)
    if p == -1:
        return
    go(v[p])
    print(a[p], end=' ')


go(p)
print()
"""
LIS를 구하고, LIS의 각 값 마다 전 값의 인덱스를 따로 V에 저장해준다.
최종적으로 LIS의 가장 큰 값(마지막 값)의 V[I]부터 재귀로 V[I] = 0가 나올 때 까지 출력해준다.
"""
