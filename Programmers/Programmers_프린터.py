def solution(priorities, location):
    data = []
    for i in range(len(priorities)):
        data.append((priorities[i], i))
    
    answer = 0
    while True:
        p, l = data.pop(0)
        if p >= max(priorities):
            answer += 1
            priorities.remove(max(priorities))
            if l == location:
                return answer
        
        else:
            data.append((p, l))
