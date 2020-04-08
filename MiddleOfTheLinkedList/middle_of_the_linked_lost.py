import sys 

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

if __name__ == '__main__':
    input = sys.stdin.read()
    nums = list(map(int, input.split()))
