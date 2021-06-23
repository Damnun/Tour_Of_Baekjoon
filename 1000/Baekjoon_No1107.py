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
