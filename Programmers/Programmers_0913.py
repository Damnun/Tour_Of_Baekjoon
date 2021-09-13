def solution(data, speed):
    answer = []
    count = 0

    while data:
        while data:
            if data[0] >= 100:
                count += 1
                data.pop(0)
                speed.pop(0)
            else:
                if count != 0:
                    answer.append(count)
                count = 0
                break

        for i in range(len(data)):
            data[i] += speed[i]
    answer.append(count)

    print(answer)
    return answer


a = [93, 30, 55]
b = [1, 30, 5]
solution(a, b)

"""
https://programmers.co.kr/learn/courses/30/lessons/42586
pop(0)를 통해 풀었는데 deque에 넣어서 popleft로 푸는게 더 빠를 것 같다
하지만 그보다 ceil을 사용하거나 다른 해법을 찾는다면 더 빠르게 풀 수 있지 않을까?
오랜만에 풀어봐서 그런지 지저분한 코드가 나온 것 같다.
더 열심히 분발해야지..
"""