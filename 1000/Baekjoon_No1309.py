n = int(input())
d = [[0] * 3 for _ in range(n + 1)]
d[0][0] = 1

for i in range(1, n + 1):
    d[i][0] = d[i - 1][0] + d[i - 1][1] + d[i - 1][2]
    d[i][1] = d[i - 1][0] + d[i - 1][2]
    d[i][2] = d[i - 1][0] + d[i - 1][1]
    for j in range(3):
        d[i][j] %= 9901
print(sum(d[n]) % 9901)
"""
D[N] = 세로로 n칸인 동물원에서 가능한 배치의 수
d[n][m] = 세로로 n칸인 동물원, 마지막 칸은 m번 방법을 사용한 배치의 수
m : 0 배치하지 않음
m : 1 왼쪽 배치
m : 2 오른쪽 배치
"""
