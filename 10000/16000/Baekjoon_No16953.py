"""
a - > b
1. 곱하기 2
2. 1을 수의 가장 오른쪽에 추가

재귀함수를 구현하여  a == b 일 경우까지
1,2번 케이스를 무한히 반복,
만약 a > b 상황이라면 해당 케이스는 중간 종료(어떻게 보면 백트래킹..?)

"""
a, b = map(int, input().split())
count = 1

def go(a, b, count):
    if a == b:
        print(count)
        exit()
    if a > b:
        return
    go(a * 2, b, count + 1)
    go(int(str(a) + "1"), b, count + 1)


go(a, b, count)
print(-1)
