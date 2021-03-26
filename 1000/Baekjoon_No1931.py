"""
n개의 회의
각 회의 l -> 시작, 끝시간
겹치지 않게 회의실을 사용할 수 있는 최대 개수
"""
from sys import stdin
time = 0
count = 0
data = []
for _ in range(int(stdin.readline())):
    data.append(tuple(map(int, stdin.readline().split())))

data.sort(key=lambda x: (x[1], x[0]))

for start, end in data:
    if start >= time:
        count += 1
        time = end
print(count)
