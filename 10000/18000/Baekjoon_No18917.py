import sys
input = sys.stdin.readline
n = int(input())
ans = 0
xor = 0

for i in range(n):
    oper = list(map(int, input().split()))
    if oper[0] == 1:
        ans += oper[1]
        xor = xor ^ oper[1]
    elif oper[0] == 2 :
        ans -= oper[1]
        xor = xor ^ oper[1]
    elif oper[0] == 3:
        print(ans)
    elif oper[0] == 4:
        print(xor)
