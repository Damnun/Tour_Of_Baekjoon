import sys
input = sys.stdin.readline

n = int(input())
data = [list(input().split()) for _ in range(n)]

data = sorted(data, key=lambda x: (int(x[3]), int(x[2]), int(x[1])), reverse=True)
print(data[0][0])
print(data[-1][0])
