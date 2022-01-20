"""
배열 돌리기 1
1. 어떤 기준으로 그룹을 만들고 1차원으로 변환
2. 1차원 배열을 R번 회전
3. 2를 다시 그룹에 넣음

이 문제에서는 바깥에서부터 얼마나 떨어졌는지에 따라 그룹을 나눔 (겹 수)
"""
n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
groups = []
groupn = min(n, m) // 2 # 그룹의 개수

# 주어진 배열을 그룹화 하여 일차원 리스트로 변환
for k in range(groupn):
    group = []
    for j in range(k, m - k): # 윗 변 그룹
        group.append(a[k][j])

    for i in range(k + 1, n - k - 1): # 오른 변 그룹
        group.append(a[i][m - k - 1])

    for j in range(m - k - 1, k, -1): # 왼쪽 변 그룹
        group.append(a[n - k - 1][j])

    for i in range(n - k - 1, k, -1): # 아랫 변 그룹
        group.append(a[i][k])
    groups.append(group)

# 변환된 일차원 리스트가 마치 환형 링 모양이라고 생각하면 편함.
for k in range(groupn):
    group = groups[k]
    l = len(group)
    index = r % l # 일정 수 이산 회전하면 결국 제자리로 돌아옴 (360도 회전은 제자리)

    # 나눠진 그룹을 다시 2차원 리스트에 배정
    for j in range(k, m - k):
        a[k][j] = group[index]
        index = (index + 1) % l
    for i in range(k + 1, n - k - 1):
        a[i][m - k - 1] = group[index]
        index = (index + 1) % l
    for j in range(m - k - 1, k, -1):
        a[n-k-1][j] = group[index]
        index = (index + 1)%l
    for i in range(n - k - 1, k, -1):
        a[i][k] = group[index]
        index = (index + 1) % l

for row in a:
    print(' '.join(map(str, row)))
