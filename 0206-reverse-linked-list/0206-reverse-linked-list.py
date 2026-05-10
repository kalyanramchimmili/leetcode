# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. 3 pointers, 1st pointer is ref node to reverse to, 2nd pointer is the current element to reverse, 3rd element is next element to traverse to
2. start with null, head, head for ptr1 , 2 ,3 
3. if ptr3 is true, move ptr3 to next, ptr2.next to ptr1, ptr1 would be ptr2 and ptr2 would go to ptr3 pos
4. to return head return ptr1, ptr2 and 3 would have gone to null when checking for last node.

time comp:- O(N)
space comp:- O(1)
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = None
        ptr2 = head
        ptr3 = head
        while ptr3:
            ptr3 = ptr3.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3
        
        return ptr1