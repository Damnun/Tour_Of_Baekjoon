def solve(a: list) -> int:  # def 함수이름(입력변수값 : 입력변수의 형식) -> 출력변수의 형식:
    ans = 0
    ans = sum(a)
    return ans


ans = input().split()
b = []
for i in ans:
    b.append(int(i))
result = solve(b)
print(result)
