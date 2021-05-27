import sys
import copy
input = sys.stdin.readline
button_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
channel = input().rstrip()
count = 0


def button_move(now, want):  # 둘 다 int
    if now == want:
        return 0
    else:
        return abs(now - want)


def button_move2(want, buttons):  # 둘 다 list
    result = 0
    while True:
        tmp = True
        for i in want:
            if int(i) not in buttons:
                tmp = False
                break

        if tmp:
            result += len(want)
            return result
        else:
            result += 1
            want = str(int(want) + 1)


def button_move3(want, buttons):  # 둘 다 list
    result = 0
    while True:
        tmp = True
        for i in want:
            if int(i) not in buttons:
                tmp = False
                break

        if tmp:
            result += len(want)
            return result
        else:
            result += 1
            if int(want) - 1 == 0:
                return 999999999
            else:
                want = str(int(want) - 1)


broken = int(input())
if broken != 0:
    broken_buttons = list(map(int, input().split()))
    for i in broken_buttons:
        if i in button_list:
            button_list.remove(i)

a = button_move(100, int(channel))
b = button_move2(copy.deepcopy(channel), button_list)
c = button_move3(copy.deepcopy(channel), button_list)
print(min(a, b, c))

