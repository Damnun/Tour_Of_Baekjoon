r, c, w = map(int, input().split())
data = [[1], [1,1]]

for i in range(2, r + w - 1):
    t = [1]
    for j in range(1, i):
        t.append(data[i-1][j-1] + data[i-1][j])
    t.append(1)
    data.append(t)
result, W = 0, 1
for i in range(r -1, r + w - 1):
    for j in range(W):
        result += data[i][c - 1 + j]
    W += 1
print(result)

"""
파스칼의 삼각형에서 원하는 삼각형 구간을 출력하는 문제
생각지도 않은 부분에서 많이 배운 것 같다.
파스칼의 삼각형의 좌우 1을 어떻게 처리해야 할지.
원하는 삼각형 구간을 어떻게 골라서 출력할 것인지
W 를 1식 카운트 증가해서 1, 2, 3, 4, ~~~ 순으로 더해준다는 발상이 참
기가막혔다.
"""