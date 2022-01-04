import sys
input = sys.stdin.readline
# 입력의 첫번째는 n의 수, 1 ~ 끝 까지 수열이 주어짐
# 입력이 0일 경우 실행 종료
# n = 주어진 값의 개수, end = 뽑아야 하는 개수
# 결과값을 저장할 result, 주어진 n개의 수의 중복 여부를 체크하는 check

def go(index, start, n, END):
    if index == END:
        print(*result)
        return

    for i in range(start, n):
        if check[data[i]]:
            continue
        check[data[i]] = True
        result[index] = data[i]
        go(index + 1, i + 1, n, END)
        check[data[i]] = False


END = 6
input_data = list(map(int, input().split()))
n = input_data[0]
while n != 0:
    data = input_data[1:]
    result = [0] * END
    check = [False] * 50
    go(0, 0, n, END)
    input_data = list(map(int, input().split()))
    n = input_data[0]
    print()


