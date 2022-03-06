def solution(brown, yellow):
    answer = []
    for i in range(1, brown + yellow + 1):
        if (brown + yellow) % i == 0:
            answer.append(i)

    if len(answer) % 2 == 1:
        ans = answer[len(answer) / 2]
        return [ans, ans]

    else:
        return [answer[len(answer) / 2], answer[len(answer) / 2 - 1]]
    return answer
