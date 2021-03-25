import sys
n, m = map(int, sys.stdin.readline().split())
data = {-1: -1}
count = 0
result = []

for _ in range(n + m):
    search = sys.stdin.readline().rstrip()
    if search in data:
        count += 1
        data[search] = 1
        result.append(search)
    else:
        data[search] = 0

print(count)
for i in sorted(result):
    print(i)

"""
마찬가지로 딕셔너리를 이용해서 푼 문제
입력 받은 문자열이 딕셔너리에 이미 존재한다면 1을 부여하고

최종적으로 1인 문자열만 result 리스트에 추가하여 정렬한 뒤 출력하였는데

in이나 count, index 등의 기본함수가 가져다주는 편리함은 물론 있지만
그마다의 시간복잡도가 상당한 경우가 많아 항상 조심해야겠다는 생각을 했다.
"""