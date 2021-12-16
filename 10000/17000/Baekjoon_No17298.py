import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
token = [-1 for _ in range(n)]
stack = []

stack.append(0)
for i in range(1, n):
    while stack and data[stack[-1]] < data[i]:
        token[stack.pop()] = data[i]
    stack.append(i)
print(*token)
