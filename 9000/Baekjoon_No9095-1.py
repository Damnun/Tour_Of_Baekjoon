def go(s, t):
    if s > t:
        return 0
    if s == t:
        return 1
    now = 0
    for i in range(1, 4):
        now += go(s + i, t)
    return now

for _ in range(int(input())):
    n = int(input())
    print(go(0, n))
    
    """
    재귀함수로 해결
    O(N^3)
    0 < N < 11 이므로 해결 가능
    """
