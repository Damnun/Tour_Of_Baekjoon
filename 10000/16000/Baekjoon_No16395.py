n, k = map(int, input().split())
pascal = [[1 for _ in range(i)] for i in range(1, n + 1)]
for i in range(2, n):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

print(pascal[n-1][k-1])

"""
파스칼의 삼각형을 dp를 이용해 파이썬으로 구현하였다.
1, 11, 111, 1111, 11111, 111111 식의 DP 테이블을 만들어주고
DP를 이용해 하나씩 더해주면 된다 (좌상, 우상)
"""