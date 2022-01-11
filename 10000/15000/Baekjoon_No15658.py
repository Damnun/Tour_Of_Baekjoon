"""
연산자의 위치, 연산자의 개수 = N - 1개
사칙연산의 수 = 4개
O(4^n - 1)
go(a, index, cur, plus, minus, mul, div)
a : 수열
index : 현재 계산중인 인덱스
cur : 현재까지 계산 값(index - 1)까지
p, m, m, d = 연산자의 개수
"""

def go(a, index, cur, plus, minus, mul, div):
    if index == n:
        return (cur, cur)
    res = []

    if plus > 0:
        res.append(go(a, index + 1, cur + a[index], plus - 1, minus, mul, div))
    if minus > 0:
        res.append(go(a, index + 1, cur - a[index], plus, minus - 1, mul, div))
    if mul > 0:
        res.append(go(a, index + 1, cur * a[index], plus, minus, mul - 1, div))
    if div > 0:
        if cur >= 0:
            res.append(go(a, index + 1, cur // a[index], plus, minus, mul, div - 1))
        else:
            res.append(go(a, index + 1, -(-cur // a[index]), plus, minus, mul, div - 1))
    ans = (max([t[0] for t in res]), min(t[1] for t in res))
    return ans

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
ans = go(a, 1, a[0], plus, minus, mul, div)
print(ans[0])
print(ans[1])
