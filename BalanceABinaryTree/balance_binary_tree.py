import sys 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = [] 
        def traverse(node: TreeNode):
            arr.append(node.val)
            if node.right and node.right is None:
                return 
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(root)
        arr.sort()
        print(arr)

        def constructTree(left, right):
            if left > right:
                return  
            mid = left + (right-left) // 2
            node = TreeNode(arr[mid])
            node.left = constructTree(left, mid-1)
            node.right = constructTree(mid+1, right)

            return node

        return constructTree(0, len(arr)-1)

if __name__ == '__main__':
    #root = [1,None,2,None,3,None,4,None,None]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    sol = Solution()
    sol.balanceBST(root)