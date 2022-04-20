import sys
from math import factorial
input = sys.stdin.readline

def solution(string, i):
    global cnt
    if i == len(a):
        cnt += 1
        if cnt == b:
            return string
    else:
        for k in a:
            if k not in string:
                res = solution(string + k, i + 1)
                if res:
                    return res

    return


while True:
    cnt = 0
    try:
        a, b = input().rstrip().split()
    except:
        break
    b = int(b)

    if factorial(len(a)) < b:
        print(a, b, '=', 'No permutation')
    else:
        print(a, b, '=', solution('', 0))
