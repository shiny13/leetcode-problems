#Uses python3
import sys
import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.sum_val = 0
        self.level_sum = {}
        def bfs(root, lvl):
            if root is None or root.val is None:
                return
            if lvl not in self.level_sum:
                self.level_sum[lvl] = root.val
            else:
                self.level_sum.update({ lvl: self.level_sum.get(lvl) + root.val })
            nextLvl = lvl+1
            bfs(root.left, nextLvl)
            bfs(root.right, nextLvl)
        bfs(root, 1)
        length = len(self.level_sum)
        #print(self.level_sum)
        return self.level_sum.get(length)

def populateTee(tree, data, i):
    if tree is None:
        return
    tree.val = data[i]
    #print("Tree i: "+ str(i) + " val: " + str(data[i])) 
    left = i*2
    right = (i*2)+1
    if left < len(data):
        tree.left = TreeNode(None)
        populateTee(tree.left, data, left)
    if right < len(data):
        tree.right = TreeNode(None)
        populateTee(tree.right, data, right)
    return

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    data = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    data.insert(0, None)
    """
    for i in range(len(data)):
        if data[i] == -1:
            data[i] = None
    """
    #print(data) 
    #construct binary tree
    tree = TreeNode(data[0])
    populateTee(tree, data, 1)

    sol = Solution()
    print(sol.deepestLeavesSum(tree))
