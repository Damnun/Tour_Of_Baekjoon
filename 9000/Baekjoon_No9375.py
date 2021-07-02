import sys
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print("0")
        continue
    result = 1
    data = []
    for _ in range(n):
        data.append(list(map(str, sys.stdin.readline().split())))

    clothes = []
    for i in range(n):
        clothes.append(data[i][1])
    tmp = set(clothes)

    for i in tmp:
        result = result * (clothes.count(i) + 1)
    print(result - 1)

"""
전체 경우에서 아예 알몸인 경우를 빼면 되는 문제
data의 의상의 종류만을 분류해서 set으로 구별하여 그 카운트를 세줌
지금은 n의 개수가 30개 밖에 안되어서 괜찮을 지 몰라도
나중에 n이 100만이 되어도, clothes에서 count 함수로 버텨낼긴 어려울 것 같다.
그때는 clothes를 딕셔너리에 저장하여 value를 1씩 증가시켜줘도 괜찮지 않을까 싶다.
"""