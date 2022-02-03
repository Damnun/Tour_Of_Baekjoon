def count(mask, words):
    cnt = 0
    for word in words:
        if (word & ((1 << 26) - 1 - mask)) == 0:
            cnt += 1
    return cnt

def go(index, k, mask, words):
    if k < 0:  # k 개의 단어를 모두 고르면 끝
        return 0
    if index == 26:  # 성공적으로 26개의 알파벳 순회가 끝나면 끝
        return count(mask, words)
    ans = 0
    t1 = go(index + 1, k - 1, mask | (1 << index), words)
    if ans < t1:  # ans < t1일 경우 t1을 ans로
        ans = t1
    if index not in [ord('a') - ord('a'), ord('n') - ord('a'), ord('t') - ord('a'), ord('i') - ord('a'), ord('c') - ord('a')]:
        t2 = go(index + 1, k, mask, words)
        if ans < t2:  # ans < t2일 경우 t2를 ans로
            ans = t2
    return ans

n, m = map(int, input().split())
words = [0] * n
for i in range(n):
    s = input()
    for x in s:
        words[i] |= (1 << (ord(x) - ord('a')))
print(go(0, m, 0, words))
