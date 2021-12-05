n = int(input())
lopes = []
result = []

for _ in range(n):
    lopes.append(int(input()))
lopes.sort(reverse= True)


for i in range(len(lopes)):
    result.append(lopes[i] * (i + 1))

print(max(result))

"""
로프와 중량, 물리학적인 성질을 띈 문제여서 너무 어렵게만 생각했나보다.
문제에서 주어진 '최대 / 최소'를 잡아내어 그리드로 풀면  바로 풀리는 문제였다.
문제를 다각적인 시야로 보는 연습을 해야지.
"""
