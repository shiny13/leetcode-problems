import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:           
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.value = 0
        def dfs(root):
            if root is not None:
                if root.val < L:
                    dfs(root.right)
                elif root.val > R:
                    dfs(root.left)
                else:
                    self.value += root.val
                    dfs(root.left)
                    dfs(root.right)
        dfs(root)
        return self.value

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    print(data)