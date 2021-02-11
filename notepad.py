n, t, c, p = map(int,input().split(" "))
index = t
cost = 0
while index < n:
    cost += c * p
    index += t
print(cost)