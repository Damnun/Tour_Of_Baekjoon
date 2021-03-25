n, m = map(int, input().split())
data = {-1: -1}

for i in range(1, n + 1):
    data[input()] = i

reverse_data = dict(map(reversed, data.items()))
for _ in range(m):
    search = input()
    if search.isdigit():
        print(reverse_data[int(search)])
    else:
        print(data[search])

"""
딕셔너리 자료형을 이용해 푼 문자열 구현문제로
딕셔너리를 뒤집어서 key-value와 value-key를 가질 수 있다는걸  알았다.
"""