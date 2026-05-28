"""
1. We can solve this que recursively, by check if the left node is less than the parent node and right is greater.
2. we have a check fun with node a low and high value intialized to inf and -inf to compare.
3. the node is comapred to see if node.left and node.right satisfy if not return False, if so continue with the loop
4. call the fun recursively to pass in node.left and low would be -inf first, high would be node.val. Similarly for right low would be node val and high be +inf.
5. after the first call, say 10 has 5 and 15 as left and right, and 15 as 6 as left. When 15, 10, +inf is passed, it will validate and when 15 calls 10, low remains 10 and high becomes the node val which is 15 for node.left.
6. This condition is used to check its previous nodes as well not just the immediate previous node to validate BST.

Time comp:- O(N)
Space comp:- O(N), for the recusrive stack.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, low=float("-inf"), high=float("inf")):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            if node.left:
                if node.left.val >= node.val:
                    return False

            if node.right:
                if node.right.val <= node.val:
                    return False

            return check(node.left, low, node.val) and check(node.right, node.val, high)

        return check(root)
