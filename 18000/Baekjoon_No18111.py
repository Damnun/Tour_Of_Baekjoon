from collections import Counter

def make_land(height):
	sec = 0
	for key in land:
		if key < height:
			sec += (height - key) * land[key]
		elif key > height:
			sec += (key - height) * 2 * land[key]
	return sec


n, m, inven = map(int, input().split())
land = []
for _ in range(n):
	land += map(int, input().split())

_sum, _len = sum(land), n * m
land = dict(Counter(land))
height, min_sec = 0, 100000000000000

for i in range(257):

	if _len * i <= _sum + inven:
		sec = make_land(i)
		if sec <= min_sec:
			min_sec = sec
			height = i

print(min_sec, height)

"""
0부터 가능한 높이까지의 모든 경우의 수를 구해서 
가장 최소 / 최대의 값을 구하는 브루트포스 문제였다.
처음에는 배열에 제일 많은 수를 구하여 그에 맞게 다른 블럭을 추가/삭제 (가지고 있는 블럭 수에 따라서)
하려고 했으나 잘 안풀렸던 것 같다. 조금 더 논리적으로 문제를 풀 수 있는 연습을 해야겠다.
"""