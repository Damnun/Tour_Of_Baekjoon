import sys
input = sys.stdin.readline
data = input().strip()
answer = set()

for i in range(len(data)):
    for j in range(i, len(data)):
        answer.add(data[i:j+1])

print(len(answer))
