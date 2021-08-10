# 조이스틱으로 알파벳 이름을 완성할 때 최소 컨트롤 횟수를 구하는 문제
# 프로그래머스 2단계
# 31.7점
def solution(name):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    reverse_alpha = alpha + []
    reverse_alpha.reverse()
    count = 0

    # 첫글자가 A 일 경우 제외해줌
    if name[0] == 'A':
        count += 1
        name = name[1:]

    # 마지막 글자가 A일 경우 제외해줌
    if name[-1] == 'A' and len(name) >= 1:
        count += 1
        name = name[:len(name) - 1]

    for i in name:
        if i == 'A':
            count += 1
            continue

        alpha_index = alpha.index(i)
        reverse_index = reverse_alpha.index(i)

        if alpha_index > reverse_index:
            count += reverse_index + 1
        else:
            count += alpha_index

        count += 1

    # 만약 처음과 끝을 제외한 문자열이 전부 A일 경우, 왼쪽으로 가면 되니 A만큼 count를 제외
    if len(name) >= 3:
        test = name[1:-1]
        if test.count('A') == len(test):
            count -= len(test)

    return count - 1