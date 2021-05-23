import heapq
from sys import stdin
heap = []

for _ in range(int(stdin.readline())):
    tmp = int(stdin.readline())

    if tmp == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")

    else:
        heapq.heappush(heap, (-tmp, tmp))

"""
파이썬의 heapq 라이브러리를 이용하여
최대 힙을 구현한 문제. 
heapq는 원래 최소 힙을 이용해서 만들어졌는데
입력값이 튜플일경우  맨 앞의 값을 기준으로 정렬하기 때문에 앞에 값에 우선순위를 넣어주는 등의 꼼수?를 통해서 최대 힙을 만들어줄 수 있다.

맨 처음에는 일반적인 리스트의 append,pop,max 등을 이용해서 풀었으나 입력값이 2^31 이라 시간초과가 나왔다.
"""