def solve(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return solve(n-1) + (2*solve(n-2))

for T in range(int(input())):
    print("#{} {}".format(T+1, solve((int(input())//10)+1)))