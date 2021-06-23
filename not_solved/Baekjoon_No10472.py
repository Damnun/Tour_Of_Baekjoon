from collections import deque
queue = deque()

flips = [[0, 1, 3], [0, 1, 2, 4], [1, 2, 5], [0, 3, 4, 6], [1, 3, 4, 5, 7],
         [2, 4, 5, 8], [3, 6, 7], [4, 6, 7, 8], [5, 7, 8]]
result = [0, 0, 0, 0, 0, 0, 0, 0, 0]

maps = []
for _ in range(3):
    maps.extend(map(str, input()))

for i in range(9):
    if maps[i] == '*':
        maps[i] = 1
    else:
        maps[i] = 0

queue.append(result)


def solve():
    count = 0
    while queue:
        count += 1
        x = queue.popleft()
        if x == maps:
            break
        for i in range(9):
            temp = x + []
            for j in flips[i]:
                if temp[j] == 0:
                    temp[j] = 1
                else:
                    temp[j] = 0
            queue.append(temp)
    print(count)


solve()
