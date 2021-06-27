_ = int(input())
loc1 = list(map(int, input().split()))
loc2 = list(sorted(set(loc1)))
loc2 = {loc2[i]: i for i in range(len(loc2))}
print(*[loc2[i] for i in loc1])

"""
딕셔너리 자료형을 이용한 좌표 압축
딕셔너리 자료형은 key : value 값으로 되어있다.
loc1의 중복을 set으로 제거하고, 정렬한 후
loc2의 값을 차례대로 key로, 0부터 값을 매겨준다
그 후 정렬되지 않은 loc1의 값을 key로 value를 불러낸다.
딕셔너리 자료형을 잘 사용하지 않고, 리스트나 튜플만을 고집했는데
딕셔너리의 중요성을 잘 알게되는 계기였다.
"""