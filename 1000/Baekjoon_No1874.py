n = int(input())
data = []  # 데이터가 들어갈 리스트 (스택)
lista = []
result = []

for i in range(n):
    data.append(int(input()))
data = data[::-1]
value = data.pop()

for i in range(1, n+1):
    lista.append(i)
    result.append('+')
    for _ in range(len(lista)):
        if lista[-1] == value:
            lista.pop()
            result.append('-')
            if not data:
                break
            value = data.pop()
        else:
            break

if not data:
    for i in result:
        print(i)
else:
    print("NO")
    
"""
파이썬의 리스트를 이용하여 스택 검사를 해주는 프로그램이다. 중간에 data가 비었는데도 pop을 연산해서 계속 오류가 발생하였는데 if data is None: 으로 검색을 하려 했는데 알고보니 파이썬에는 빈 공간이 있어도 None으로는 탐색이 불가하고 if not data:로 true/false 식으로 받아와야 했다. 유의하자

8
4
3
6
8
7
5
2
1
"""