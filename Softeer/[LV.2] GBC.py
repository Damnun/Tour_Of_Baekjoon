import sys
input = sys.stdin.readline

n, m = map(int,input().split())
limit = [0] * 101
cur = 1

for _ in range(n):
    section, speed = map(int, input().split())
    for i in range(cur, cur + section):
        limit[i] = speed
    cur = cur + section

result = 0 
cur = 1

for _ in range(m):
    section, speed = map(int, input().split())
    for i in range(cur, cur + section):
        result = max(result, speed - limit[i])
    cur = cur + section

print(result)
