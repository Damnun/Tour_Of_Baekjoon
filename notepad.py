def solution(n):
    answer = 0
    tmp = str(n)
    print(tmp[::-1])
    for i in tmp[::-1]:
        answer += int(i) * (3**int(i))
    return answer

print(solution('125'))
