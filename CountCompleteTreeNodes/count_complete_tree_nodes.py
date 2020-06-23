import sys 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.nodes = 0

        def traverse(_node: TreeNode):
            if _node is None:
                return 
            self.nodes += 1
            traverse(_node.left)
            traverse(_node.right)
        traverse(root)

        return self.nodes 

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
