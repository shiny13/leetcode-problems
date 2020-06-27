import sys 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        
        if not root.left and not root.right:
            return int(root.val)
        
        if root.left: root.left.val = 10*root.val + root.left.val
        if root.right: root.right.val = 10*root.val + root.right.val
            
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)

if __name__ == '__main__':
    # test 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    # test 2
    node = TreeNode(4)
    node.left = TreeNode(9)
    node.right = TreeNode(0)
    node.left.left = TreeNode(5)
    node.left.right = TreeNode(1)

    sol = Solution()
    #print(sol.sumNumbers(root))
    print(sol.sumNumbers(node))
