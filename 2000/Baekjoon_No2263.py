import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

node = [0] * (n + 1)
for i in range(n):
    node[inorder[i]] = i

def pre(ins, ine, pos, poe):
    if (ins > ine) or (pos > poe):
        return

    root = postorder[poe]

    l = node[root] - ins
    r = ine - node[root]

    print(root, end=" ")
    pre(ins, ins + l - 1, pos, pos + l - 1)
    pre(ine - r + 1, ine, poe - r, poe - 1)

pre(0, n - 1, 0, n - 1)
