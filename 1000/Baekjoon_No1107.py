N = int(input())
M = int(input())
remote_list = {str(i) for i in range(10)}

if M > 0:
    remote_list -= set(map(str, input().split()))

current = 100
minimum = abs(current - N)  # +/- 만을 이용

for channel in range(1000001):
    for i in range(len(str(channel))):
        if str(channel)[i] not in remote_list:
            break
        elif len(str(channel)) - 1 == i:
            minimum = min(minimum, abs(channel - N) + len(str(channel)))
print(minimum)

"""
이것도 꽤나 고전했던 문제.
브루트포스로 난도 있는 문제를 푸는게 어렵다.
리모컨의 고장난 버튼을 set으로 제외해주고
단순히 +/-를 이용할 때, 사용할 수 없는 버튼을 제외하고 최적의 값을 (min)으로 구해주었다.
"""