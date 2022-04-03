a, b, c = map(int, input().split(' '))


def solution(b):
    if b == 1:
        return a % c
    if b % 2 == 0:
        l = solution(b // 2)
        return l * l % c
    else:
        l = solution(b // 2)
        return l * l * a % c


print(solution(b))
