"""
1. Define height fun from balanced binary tree method
2. Intialize a diameter to find the max diameter for left+right.
3. Return the max diameter recorded

time comp:- O(N)
space comp:- O(h) -> recursive track.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        
        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            leftHeight = height(node.left)
            rightHeight = height(node.right)
            diameter = max(diameter, leftHeight+rightHeight)

            return 1+max(leftHeight,rightHeight)
        
        height(root)
        return diameter
