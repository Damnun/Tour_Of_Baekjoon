from collections import deque
n, k = map(int, input().split())

visit = [0 for i in range(100001)] # 0~100000 까지의 방문경로를 visit으로 hash해줌

queue = deque()
queue.append([n, 0]) #n에서 시작, 0은 카운트의 수


while queue:
    p, d = queue[0][0], queue[0][1] # p에는 시작점, d에는 카운트가 저장
    if p == k: # 시작점이 k(동생)의 위치와 같다면 종료
        break
    queue.popleft() # 큐의 제일 왼쪽에 있는 data pop
    visit[p] = 1 # 방문처리
    if p - 1 >= 0 and visit[p - 1] == 0: # 시작점이 0보다 크고, -1 지점을 방문하지 않았을 경우
        queue.append([p - 1, d + 1])
    if p + 1 <= 100000 and visit[p + 1] == 0: # 시작점이 100000보다 작고, +1 지점을 방문하지 않았을 경우
        queue.append([p + 1, d + 1])
    if p * 2 <= 100000 and visit[p * 2] == 0: # 시작점이 100000보다 작고, *2 지점을 방문하지 않았을 경우
        queue.append([p * 2, d + 1])
print(queue[0][1])