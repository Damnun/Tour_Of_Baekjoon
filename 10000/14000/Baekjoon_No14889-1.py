"""
팀 번호를 0번팀 / 1번팀이라 하면 비트마스크로 해결할 수 있음.
0 ~ (1 << N) 까지 모든 번호를 0/1로 나누어줌
"""

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range((1 << n)):
    first = [] # 0번
    second = [] # 1번
    for j in range(n):
        if (i & (1 << j)) > 0:
            first += [j]
        else:
            second += [j]
    if len(first) != n // 2:
        continue
    t1 = 0
    t2 = 0
    for l1 in range(n // 2):
        for l2 in range(n // 2):
            if l1 == l2:
                continue
            t1 += s[first[l1]][first[l2]]
            t2 += s[second[l1]][second[l2]]
    diff = abs(t1 - t2)
    if ans == -1 or ans > diff:
        ans = diff
print(ans)
