def solution(msg):
    dic = {chr(i): i+1-ord('A') for i in range(ord('A'), ord('Z')+1)}
    answer, start, end = list(), 0, 0
    while end < len(msg):
        if msg[start:end+1] in dic:
            end += 1
        else:
            dic[msg[start:end+1]] = len(dic)+1
            answer.append(dic[msg[start:end]])
            start, end = end, end
    answer.append(dic[msg[start:end+1]])
    return answer
print(solution("ABABAABAB"))
