"""
1. slow and fast pointers, inc fast pointer by 2 steps and slow by 1
2. if they meet then there is loop, if not no loop, check he intial condition, if we have no nodes in ll and only one node with no cycle and return false early

time comp:- o(n)
space :- o(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if (not head) or (not head.next):
            return False

        fast = head.next
        slow = head

        while fast and fast.next:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False
