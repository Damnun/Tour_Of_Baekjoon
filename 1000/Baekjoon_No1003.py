for _ in range(int(input())):
    data = int(input())
    result = [[1, 0], [0, 1], [1, 1]]

    if data >= 2:
        for i in range(2, data):
            result.append([result[i][1], result[i][0] + result[i][1]])

    print(result[data][0], result[data][1])

"""
DP로 피보나치 수열의 0과 1 출력 포인트를 찾아서 카운트 해주는 프로그램인데 그냥 수열의 일반항을 찾아서 풀어버렸다. 나중에 dp가 익숙해지면 정론으로 다시 풀어봐야겠다.
"""