def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]
    M, m = {}, {}
    
    for i in range(len(nums)):
        M[(i, i)] = nums[i]
        m[(i, i)] = nums[i]
    
    for d in range(1, len(nums)):
        for i in range(len(nums)):
            j = i + d
            if j >= len(nums):
                continue
    
            maxc, minc = [], []
            for k in range(i + 1, j + 1):
                if ops[k - 1] == '-':
                    mx = M[(i, k - 1)] - m[(k, j)]
                    mn = m[(i, k - 1)] - M[(k, j)]
                    maxc.append(mx)
                    minc.append(mn)
                else:
                    mx = M[(i, k - 1)] + M[(k, j)]
                    mn = m[(i, k - 1)] + m[(k, j)]                
                    maxc.append(mx)
                    minc.append(mn)

            M[(i, j)] = max(maxc)
            m[(i, j)] = min(minc)
    
    return M[(0, len(nums) - 1)]
