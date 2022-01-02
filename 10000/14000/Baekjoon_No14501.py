"""
버는 돈의 최댓값을 구하기
i일 : T[i]일 걸리고, P[i]원 번다

각 날짜마다 선택지
1. 상담을 한다
2. 상담을 안 한다
이에 따라 결정되는 것
1. 날짜
2. 수입
"""
import sys
input = sys.stdin.readline

def go(day, income):
    global ans
    # income : day - 1일 까지의 수익
    # 정답을 찾은 경우
    if day == n:
        ans = max(ans, income)
        return
    if day > n:
        return
    go(day + t[day], income + p[day]) # 상담을 할 때
    go(day + 1, income) # 상담을 안 할때


ans = 0
n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)
for i in range(n):
    t[i], p[i] = map(int, input().split())
go(0, 0)
print(ans)
