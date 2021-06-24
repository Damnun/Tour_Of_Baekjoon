import heapq
import sys

T = int(sys.stdin.readline())  # 테스트 케이스
for _ in range(T):
    result = []
    k = int(sys.stdin.readline())  # 연산의 개수
    for _ in range(k):
        op, data = sys.stdin.readline().split()
        data = int(data)
        if op == 'I':
            heapq.heappush(result, data)
        else:
            if len(result):
                if data == 1:
                    result.pop(result.index(heapq.nlargest(1, result)[0]))
                else:
                    heapq.heappop(result)
            else:
                pass
    if not len(result):
        print("EMPTY")
    else:
        print(heapq.nlargest(1, result)[0], heapq.nsmallest(1, result)[0])

"""
시간초과 이지만 알아두면 유용할 지식일 것 같다.
heapq를 이용한 새로운 풀이방법
컬렉션 내부에서 가장 크거나 작은 N개의 아이템을 찾는법
heapq.nlargest(n, iterable, key=None)
heapq.nsmallest(n, iterable, key=None)
grade = {
    {'name': 'Steve', 'grade': 80}
    {'name': 'David', 'grade': 90},
    {'name': 'Tony', 'grade': 40},
    {'name': 'Grace', 'grade': 100}
}
heapq.nlargest(2, grades, lambda s: s['grade']) -> [Grace, David]
방식으로 사용할 수 있다. (단 N이 1일 경우 max나 min 함수를 사용해보자)
"""