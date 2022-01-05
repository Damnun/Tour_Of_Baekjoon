def go(index, num):
    if index == n + 1:
        if ok(num):
            ans.append(num)
        return

    for i in range(10):
        if check[i]:
            continue
        if (index == 0 or good(int(num[index - 1]), i, a[index - 1])):
            check[i] = True
            go(index + 1, num + str(i))
            check[i] = False


def ok(num):
    for i in range(n):
        if a[i] == '<':
            if num[i] > num[i + 1]:
                return False
        elif a[i] == '>':
            if num[i] < num[i + 1]:
                return False
    return True


def good(x, y, op):
    if op == '<':
        if x > y:
            return False
    if op == '>':
        if x < y:
            return False
    return True

n = int(input())
a = input().split()
check = [False] * 10
ans = []
go(0, '')
ans.sort()
print(ans[-1])
print(ans[0])


"""
주어진 부등호의 리스트들을 모두 성립시킬 수 있도록 사이에 숫자를 배열시켜야 하는 문제
0~9까지 10개의 숫자를 사이에 넣는 방법의 수는 10! = 약 362만정도로 brute force로 해결할 수 있다
재귀함수를 통해 index(각 자리)마다 check(중복된 값이 없게) num(현재까지 만들어진 수)를 생성해주는데,
부등호 초반에 어긋난 부분이 있다면, 어차피 돌려도 쓸모 없는 실행이기에, good이라는 함수를 통해
중간에 부등호가 어긋난다면 실행을 취소하는(백트래킹 기법)을 사용하였따.
"""
