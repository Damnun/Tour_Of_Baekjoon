"""
1, 2, 3, 4, 5
2, 1, 2, 3, 2, 4, 2, 5
3, 3, 1, 1, 2, 2, 4, 4, 5, 5

1 // 2 3 4 5 반복
2 // 1 반복 3반복 4 반복 5반복


"""

import itertools

N, M = map(int, input().split())
card = list(map(int, input().split()))
ans = 0

for i in itertools.combinations(card, 3):
    card_sum = sum(i)
    if ans < card_sum and card_sum <= M:
        ans = sum(i)
print(ans)