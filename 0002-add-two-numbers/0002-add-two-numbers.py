# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1. create a ans linked list with 0 -> None
2. add a carry flag for next addition
3. for uneven linkedlists use 0s to add
4. if sum is greater than 10 then flag is true else not, and add the ones digit of it to the ans linked list
5. and iterate until end of the list
6. and return the ans list from 0.
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        current = ans
        prev_rem = 0
        
        while l1 or l2 or prev_rem:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + prev_rem
            prev_rem = total//10
            total = total%10
            
            current.next = ListNode(total)
            current = current.next

            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        
        return ans.next


