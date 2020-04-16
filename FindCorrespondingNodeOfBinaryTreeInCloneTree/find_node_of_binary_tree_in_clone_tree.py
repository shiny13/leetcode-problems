# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [cloned]
        while (stack):
            curr_node = stack.pop(0)
            if curr_node.val == target.val:
                return curr_node
            else:
                if curr_node.left != None:
                    stack.append(curr_node.left)
                if curr_node.right != None:
                    stack.append(curr_node.right)
            