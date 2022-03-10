def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 가중치를 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # Kruskal 가중치 집합 생성
    
    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]]) # set 자료형의 추가 update (not append)
                answer += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return answer
