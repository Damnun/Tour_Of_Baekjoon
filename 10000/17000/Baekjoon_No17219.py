import sys
N, M = map(int, input().split())
data = [list(sys.stdin.readline().split()) for _ in range(N)]
data_dic = {i[0]: i[1] for i in data}
search = [list(sys.stdin.readline().split()) for _ in range(M)]

for i in search:
    print(data_dic[i[0]])

"""
딕셔너리를 이용하여 시간단축 성공!
처음에는 무작정 data와 search 리스트에 넣어놓은 것을 루프로 해결하려 했지만
그 경우의 수가 너무 많아져 시간 초과가 나타났다.
이를 저번에 배웠던 딕셔너리를 사용할 수 없을 까 생각해보다 문제를 성공시켰다.
data에 [0]과 [1]에 들어있는 것을 key-value 구조로 변환시켜
search에 들어있는 것들을 O(1)로 계산할 수 있었다.
"""