def solution(n):
    tmp = n + 1
    count = 0
    n_count = 0
    answer = 0

    while n > 0:
        if n % 2 == 1:
            n_count += 1
        n //= 2

    while True:
        if count == n_count:
            answer = tmp - 1
            break
        count = 0

        k = tmp
        while k > 0:
            if k % 2 == 1:
                count += 1
            k //= 2

        tmp += 1
    
    return answer

print(solution(78))

"""
programmers 문제풀이 1
"""