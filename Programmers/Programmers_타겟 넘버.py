from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append((0, 0))
    while queue:
        cur, i = queue.popleft()
        if i == len(numbers):
            if cur == target:
                answer += 1
        else:
            n = numbers[i]
            queue.append((cur + n, i + 1))
            queue.append((cur - n, i + 1))
    return answer
