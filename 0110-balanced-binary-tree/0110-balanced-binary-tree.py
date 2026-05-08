"""
1. build a function to check max depth of a tree (that fun is checking the max height from leaf to head node)
2. call that fun to get left tree height and right tree height and check the abs diff btw them is atmost 1 if not return False
3. repeat the same for every node in the tree using recursion

time comp:- O(n^2)
space comp:- O(n) recursion stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)
