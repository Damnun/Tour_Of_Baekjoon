n, w = map(int, input().split())
bag = [tuple(map(int, input().split())) for _ in range(n)]

knap = [0 for _ in range(w + 1)]

for i in range(n):
    for j in range(w, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])
print(knap[-1])

"""
처음으로 풀어보는 골드문제이다.
DP를 이용해서 배낭에 문제가 요구하는 최적의 짐을 싸야하는데
배낭을 넣을 수 있는 테이블을 가상으로 설정하여 (행렬이나 N차원배열)
큰 무게에서부터 넣을 수 있는 무게를 빼고
남는 무게 값이 있다면 그 값을 더해서 최적의 값을 구해내는 방식이다
여러모로 많이 사용할 것 같다.
열심히 연습해야겠다!
"""