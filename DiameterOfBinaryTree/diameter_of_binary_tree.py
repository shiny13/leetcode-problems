# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
			return 0
	
		def max_depth(node: TreeNode, vals: List[int]) -> int:
			if not node:
				return 0
	
			left: int = max_depth(node.left, vals)
			right: int = max_depth(node.right, vals)
	
			vals.append(left + right)
	
			if left > right:
				return left + 1
			else:
				return right + 1
	
		nums: List[int] = []
		ret = max_depth(root, nums)
	
		return max(nums)

if __name__ == '__main__':
    sol = Solution()