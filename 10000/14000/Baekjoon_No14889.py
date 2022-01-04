"""
1. 백트래킹
2. N명, N/2명으로 스타트/링크 팀으로 나눔
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
        if len(first) != n // 2:
            return -1
        if len(second) != n // 2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(n // 2):
            for j in range(n // 2):
                if i == j:
                    continue
                t1 += s[first[i]][first[j]]
                t2 += s[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff
    ans = -1
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

"""
Brute Force로 해결한 문제방법 -> 재귀 중간에 N/2를 넘어간 팀이 나오게 되면 중단 -> 백트래킹 이용 가능
"""
