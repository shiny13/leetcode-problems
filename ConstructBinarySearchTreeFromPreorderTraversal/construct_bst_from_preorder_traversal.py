import sys
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        def insertIntoTree(root: TreeNode, val: int):
            while True:
                if root.val > val:
                    if not root.left:
                        root.left = TreeNode(val)
                        break
                    else:
                        root = root.left
                        print("else root.left: " + str(root.left))
                else:
                    if not root.right:
                        root.right = TreeNode(val)
                        break
                    else:
                        root = root.right
                        print("else root.right: " + str(root.right))
        head = root 
        for i in range(1, len(preorder)):
            head = root 
            insertIntoTree(head, preorder[i])

        return head

if __name__ == '__main__':
    input = sys.stdin.read()
    preorder = list(map(int, input.split()))

    sol = Solution()
    sol.bstFromPreorder(preorder)