"""
-10 ~ 10 까지 N개의 정수로 이루어진 수열 A (N <= 10)
S[i][j] = A[i] ~ A[j] 까지의 합,
S[i][j]가 0보다 크면 +, 작으면 -, 같으면 0을 출력
S가 주어졌을 때, 가능한 A를 찾는 문제

각 자리마다 21가지의 수를 구해 넣어주저야 함
O(21^10)은 너무 큰 수로 BRUTE FORCE로는 해결이 어려움


----시간초과를 해결 할 방법 첫번째----
s[i][i] = A[i]의 부호
s[i][i] > 0 1~ 10
        = 0 0
        < 0 -10 ~ -1
로 경우의 수를 10^10로 줄일 수 있다.
하지만 10^10은 100억으로 시간초과.

----두번째----
i번째의 수를 정하면 S[j][i]의 부호를 모두 검사할 수 있다.
"""

def check(index):
    s = 0
    for i in range(index, -1, -1):
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True

def go(index):
    if index == n:
        return True
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and go(index + 1)

    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and go(index + 1):
            return True
    return False


n = int(input())
s = input()
sign = [[0] * n for _ in range(n)]
ans = [0] * n
cnt = 0
for i in range(n):
    for j in range(i, n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1
go(0)
print(' '.join(map(str, ans)))
