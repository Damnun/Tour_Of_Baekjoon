def solution(number, k):
    data = []
    for i in range(len(number)):
        while data and k > 0 and data[-1] < number[i]:
            data.pop()
            k -= 1
        data.append(number[i])
    return ''.join(data[:len(data) - k])
