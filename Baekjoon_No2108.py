"""
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
"""
import sys
from collections import Counter
loop = int(sys.stdin.readline())
result = []
for _ in range(loop):
    result.append(int(sys.stdin.readline()))

print("%.f"%(sum(result)/loop))

result.sort()
index = len(result) // 2
print(result[index])    # 중앙값

# ----------------------------------------------------- 최빈값 시작
k = Counter(result).most_common()

if len(result) > 1:                          # 만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:                                    # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
        print(k[0][0])
else:
    print(result[0])

# ----------------------------------------------------- 최빈값 종료

print(max(result) - min(result))    # 범위
