N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
sorted_data = sorted(data, key=lambda x: (-x[0], x[1], x[2]))
print(data.index(sorted_data[0]) + 1)

"""
1. 문제 점수의 총 합 (내림차순 이므로 lambda 정렬시 - 값으로 줘야 함.)
2. 제출 횟수가 적을수록
3. 업로드 시간이 빠를수록

3가지 조건을 지니고 정렬 하는 문제
정렬 시에 - 값을 주는 이유는 내림차순 정렬을 해주기 위함임
같은 방식으로 우선순위 큐에서도 기본적으로 오름차순으로 정렬이 되는 값을
우선순위에 - 값을 매겨서 내림차순으로 정렬시킬 수 있음

"""