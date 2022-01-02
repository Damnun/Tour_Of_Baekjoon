"""
1. 길이는 L
2. 소문자
3. 최소 한개의 모음
4. 최소 두개의 자음
5. 증가하는 순서
6. 문자 종류 C가지

문자 종류 C가지
각각의 알파벳을 사용한다 / 사용하지 않는다의 경우(2가지)
O(2^c)
3 <= L <= C <= 15 이므로
2^15 -> 32768, 충분히 해결 가능

"""
def check(password):
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


def go(l, alphabet, cur_pass, index):
    if len(cur_pass) == l:
        if check(cur_pass):
            print(cur_pass)
        return
    if index == len(alphabet):
        return
    go(l, alphabet, cur_pass + alphabet[index], index + 1)
    go(l, alphabet, cur_pass, index + 1)


l, c = map(int, input().split())
alphabet = input().split()
alphabet.sort()
go(l, alphabet, "", 0)
