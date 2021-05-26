loop = int(input())

for _ in range(loop):
    left = []
    right = []
    data = input()

    for i in data:
        if i == '>':
            if right:
                left.append(right.pop())
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    print("".join(left)+"".join(reversed(right)))

"""
커서를 기준으로 좌 우에 리스트(스택)가 있다고 생각을 하고 구현을 하면 되는 문제였다.
처음에는 index 변수를 지정하여 <>- 입력에 따라서 +/-를 해주려 했으나 시간상으로도 이론상으로도 너무 복잡했다.
좌 우를 나누는 벽이 있다고 생각하고, 이를 넘나드는 과정을 그린다고 생각하면 풀리는 문제였다.
조금 더 프로그래밍적인 관점에서 사고하는 연습을 많이 해야겠다고 느꼈다.
"""
