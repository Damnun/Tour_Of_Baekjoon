N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = []


def solution(x, y, N):
    color = matrix[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != matrix[i][j]:
                solution(x, y, N//2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)


solution(0, 0, N)
print(result.count(0))
print(result.count(1))

"""
분할 정복을 이용한 색종이 분할 문제. 색종이를 N, N/2, N/4, N/8 등으로 쪼개면서 1칸이 될 때 까지 쪼개어 구역을 나누어 주었다. 처음엔 BFS로 풀려고 하다가 실패했는데, 다시 시도해봐야겠다.
"""