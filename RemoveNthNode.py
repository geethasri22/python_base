# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node pointing to head
        # This helps handle cases like removing the first node
        temp = ListNode(0, head)

        # Initialize two pointers at dummy
        fast = temp
        slow = temp

        # Move fast pointer n+1 steps ahead
        # So the gap between fast and slow is n nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Now slow is right before the node to remove
        slow.next = slow.next.next

        # Return the new head (dummy.next skips the dummy node)
        return temp.next
