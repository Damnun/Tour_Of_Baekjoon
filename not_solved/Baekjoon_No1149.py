n = int(input())
r, g, b = map(int, input().split())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))
for i in range(1, len(cost)):
    