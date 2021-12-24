def solution(name):
    minimum_move = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    i, answer = 0, 0
    while True:
        answer += minimum_move[i]
        minimum_move[i] = 0
        if sum(minimum_move) == 0:
            break
        l, r = 1, 1
        while minimum_move[i - l] == 0:
            l += 1
        while minimum_move[i + r] == 0:
            r += 1
        answer += l if l < r else r
        i += -l if l < r else r
    return answer

print(solution(input()))
