from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append([a, ""])

    while queue:
        number, result = queue.popleft()

        dn = (number * 2) % 10000
        if dn == b:
            return result + "D"
        elif arr[dn] == 0:
            arr[dn] = 1
            queue.append([dn, result + "D"])

        sn = number - 1 if number != 0 else 9999
        if sn == b:
            return result + "S"
        elif arr[sn] == 0:
            arr[sn] = 1
            queue.append([sn, result + "S"])

        ln = int(number % 1000 * 10 + number / 1000)
        if ln == b:
            return result + "L"
        elif arr[ln] == 0:
            arr[ln] = 1
            queue.append([ln, result + "L"])

        rn = int(number % 10 * 1000 + number // 10)
        if rn == b:
            return result + "R"
        elif arr[rn] == 0:
            arr[rn] = 1
            queue.append([rn, result + "R"])


for i in range(int(input())):
    a, b = map(int, input().split())
    arr = [0 for i in range(10000)]
    print(bfs())

"""
D/S/L/R 각각의 계산 결과를 BFS를 통해 가지를 뻗어나가며 문제를 해결한다.
처음에는 while을 이용하여 입력 값이 결과 값이 나올 때 까지 조건을 반복해야 하나?
하는 마음으로 풀었다가 호되게 당해버렸다. BFS는 아직 그래프에서만 사용한다는
고정관념이 있었던 것 같다. 문득 풀이를 보았을 때 머리를 한대 맞은 기분이었다.
아직 아직 멀었나보다. 더 열심히 공부하자
"""