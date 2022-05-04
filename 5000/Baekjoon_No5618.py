import sys
input = sys.stdin.readline

def solution(a, b):
    if(a == 0):
        return b
    return solution(b % a, a)


n = int(input())
a = list(map(int, input().split()))
b = solution(a[0], solution(a[1], a[-1]))
for i in range(1, (b // 2) + 1):
    if b % i == 0:
        print(i)
print(b)
