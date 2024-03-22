from collections import deque


def solution(tickets):
    answer = []
    tickets.sort(key = lambda x: (x[0], x[1]))
    queue = deque([(["ICN"], tickets)])
    
    while queue:
        path, ticket = queue.popleft()
        
        if len(ticket) == 0:
            answer = path
            break
        
        valid_idx = -1
        for i in range(len(ticket)):
            if ticket[i][0] == path[-1]:
                valid_idx = i
                break
        
        if valid_idx == -1:
            continue
        
        while valid_idx < len(ticket) and ticket[valid_idx][0] == path[-1]:
            queue.append((path + [ticket[valid_idx][1]], ticket[:valid_idx] + ticket[valid_idx + 1:]))
            valid_idx += 1
    
    return answer
    
