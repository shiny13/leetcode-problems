import sys 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        output = ''
        while head is not None:
            output += str(head.val)
            head = head.next 

        print(int(output,2))
        return int(output,2)

if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #sample input
    listNode = ListNode(1)
    listNode.next = ListNode(0)
    listNode.next.next = ListNode(1)
    sol = Solution()
    sol.getDecimalValue(listNode)
