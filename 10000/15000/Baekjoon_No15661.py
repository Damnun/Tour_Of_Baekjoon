"""
1. 백트래킹
2. 최소 1명 이상으로 스타트/링크 팀으로 나눔
3. 1~N까지 배정
4. 두 팀의 능력치를 구하고 차이의 최소를 구하야함.
5. S[i][j] = i번 사람과 j번 사람이 같은 팀일 때 팀에 더해지는 능력치
6. 팀의 능력치 : 팀에 속한 모든 s[i][j]쌍의 합
2^n가지 경우의 수, n의 최대 = 20
O(2^n) 약 100만가지로 실행 가능


함수
- index : 사람을 어떤 팀에 넣을지
- first : 1번 팀, second : 2번 팀
- index == n 일 경우 함수 종료

"""

def go(index, first, second):
    if index == n:
        if 1 > len(first) or len(first) > n:
            return -1
        if 1 > len(second) or len(second) > n:
            return -1

        t1 = 0
        t2 = 0

        for i in range(len(first)):
            for j in range(len(first)):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]

        for i in range(len(second)):
            for j in range(len(second)):
                if i == j:
                    continue
                t2 += s[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff

    ans = -1
    if len(first) >= n:
        return -1
    if len(second) >= n:
        return -1

    t1 = go(index + 1, first + [index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index + 1, first, second + [index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(go(0, [], []))
