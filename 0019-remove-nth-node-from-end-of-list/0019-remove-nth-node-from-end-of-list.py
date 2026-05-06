"""
1. 2 pointer problem in linked list, both start at head, the fast pointer gets a head start by n steps. This maintains a n steps gap which helps us determine the node to delete
"
-> 1(s)(f)->2->3->4->5 -> Null

-> 1(s)->2->3(f)->4->5 -> Null
    <-2 steps->

-> 1->2(s)->3->4(f)->5 -> Null

-> 1->2->3(s)->4->5(f) -> Null
"
2. next, we check if fast is null, cases when we have to delete first node, len is 5 and n is 5, fast would move 5 steps, reaching null, if fast is null simply return head.next eliminating first element
3. else, until fast.next is not null inc fast and slow by 1 step
4. the mom fast reaches null, then replace slow.next with slow.next.next, skipping the node we want to delete and then return ans

time comp:- o(n)
space:- o(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head

        if fast.next == None and n == 1:
            head = head.next
            return head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
