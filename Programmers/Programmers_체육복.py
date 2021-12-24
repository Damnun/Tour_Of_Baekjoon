def solution(n, lost, reverse):
    result = 0

    # 도난을 당한 학생 리스트
    lost_list = [-99 for _ in range(n)]
    for i in lost:
        lost_list[i - 1] = i

    # 여벌을 가져온 학생 리스트
    reverse_list = [0 for _ in range(n)]
    for i in reverse:
        reverse_list[i - 1] = i

    # 여벌을 가져온 학생이 도난 당했을 경우
    for i in reverse_list:
        if i in lost:
            reverse_list[i - 1] = 0
            lost_list[i - 1] = -99

    for i in reverse_list:
        if i > 0:
            data = [-1, 1]
            for j in data:
                if i + j in lost_list:
                    lost_list[i + j - 1] = -99
                    break

    result = lost_list.count(-99)
    return result


n = int(input())
lost = list(map(int, input().split()))
reverse = list(map(int, input().split()))
print(solution(n, lost, reverse))
