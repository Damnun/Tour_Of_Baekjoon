def go(a, l):
    n = len(a)  # 입력받은 행/열의 길이
    c = [False] * n  # x번 칸에 경사로를 놓았다면 True/False
    for i in range(1, n):
        if a[i - 1] != a[i]:
            diff = abs(a[i] - a[i - 1])
            if diff != 1:
                return False
            if a[i - 1] < a[i]:
                for j in range(1, l+1):
                    if i - j < 0:
                        return False
                    if a[i - 1] != a[i-j]:
                        return False
                    if c[i - j]:
                        return False
                    c[i - j] = True
            else:
                for j in range(l):
                    if i + j >= n:
                        return False
                    if a[i] != a[i + j]:
                        return False
                    if c[i + j]:
                        return False
                    c[i + j] = True
    return True


n, l = map(int,input().split()) # 맵의 크기 n과 경사로의 길이 l
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# 모든 행을 연산
for i in range(n):
    d = a[i]
    if go(d, l):
        ans += 1

# 모든 열을 연산
for j in range(n):
    d = [a[i][j] for i in range(n)] # d 에 i번째 열을 넣어줌
    if go(d, l):
        ans += 1
print(ans)

