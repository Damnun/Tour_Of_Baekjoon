dp = [[[0]*21 for _ in range(21)] for __ in range(21)]


def solve(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        return solve(20, 20, 20)

    if dp[x][y][z]:
        return dp[x][y][z]

    if x < y < z:
        dp[x][y][z] = solve(x, y, z - 1) + solve(x, y - 1, z - 1) - solve(x, y - 1, z)
        return dp[x][y][z]

    dp[x][y][z] = solve(x - 1, y, z) + solve(x - 1, y - 1, z) + solve(x - 1, y, z - 1) - solve(x - 1, y - 1, z - 1)
    return dp[x][y][z]


while True:
    a, b, c = map(int, input().split())

    if a == b == c == -1:
        break

    print("w(%d, %d, %d) = %d" % (a, b, c, solve(a, b, c)))

"""
DP 메모이제이션에 대해서 묻는 문제.
재귀함수의 계산 결과를 DP에 저장해두고
해당 DP를 호출하여 0이 아닐경우 값이 있다는 뜻이므로 계산을 스킵하여
프로그램 속도를 비약적으로 향상시킴
실제로 DP를 사용하지 않고 해당 알고리즘을 풀게 된다면 숫자 15를 넘어가면 연산이 거의 불가할 것이다.
"""