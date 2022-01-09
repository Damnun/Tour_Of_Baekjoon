import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())
data = []
data.append(a / c + b / d)
data.append(c / d + a / b)
data.append(d / b + c / a)
data.append(b / a + d / c)
print(data.index(max(data)))
