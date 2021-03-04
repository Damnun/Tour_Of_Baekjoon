from collections import deque

data_count = int(input())
data = deque()

for i in range(data_count):
    data.append(i+1)

while True:
    if len(data) == 1:
        break
    data.popleft()
    data.append(data.popleft())
print(data[0])
    