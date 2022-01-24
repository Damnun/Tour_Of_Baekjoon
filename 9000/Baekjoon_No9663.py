n = int(input())
a = [[False] * n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2 * n - 1)
check_dig2 = [False] * (2 * n - 1)

def check(row, col):
    if check_col[col]: # 수직 검사
        return False
    if check_dig[row + col]: # 오른 대각선 검사
        return False
    if check_dig2[row - col + n - 1]: # 왼 대각선 검사
        return False
    return True # 전부 통과하면 True


def calc(row):
    if row == n: # 모든 행을 방문 했을 경우
        return 1
    ans = 0 # 정답 개수
    for col in range(n):
        if check(row, col):
            check_dig[row + col] = True
            check_dig2[row - col + n - 1] = True
            check_col[col] = True
            a[row][col] = True

            ans += calc(row + 1)

            # 순회가 끝나고 다음 col을 위해 모두 False로 전환.
            check_dig[row + col] = False
            check_dig2[row - col + n - 1] = False
            check_col[col] = False
            a[row][col] = False
    return ans

print(calc(0))
