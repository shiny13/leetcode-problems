import sys 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return 0
            if node.val != 0:
                return dfs(node.left)+dfs(node.right)
            else:
                total=0
                for T_node in (node.left,node.right):
                    if T_node is None:continue
                    if T_node.left is not None: total+=T_node.left.val
                    if T_node.right is not None: total+=T_node.right.val
                return total+dfs(node.left)+dfs(node.right)
        return dfs(root)

if __name__ == '__main__':
    root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
    sol = Solution()

