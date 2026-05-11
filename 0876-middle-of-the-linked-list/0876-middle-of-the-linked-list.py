"""
1. fast and slow pointer method, move fast pointer to 2 steps and slow to one
2. for even ll, fast would be at n-1 node, so if fast.next exists, then move slow one step further and return slow

time comp:- O(N)
space comp:- O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next:
            slow = slow.next
        
        return slow
        