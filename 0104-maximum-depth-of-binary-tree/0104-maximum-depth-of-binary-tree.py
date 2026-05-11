"""
1. similar to diameter or balanced binary tree, find the max height of a tree from node
2. make a height fun for left and right node, return 1+max(left,hight) would give max height of left or right and add in recursive way
3. return the height from node

time comp:- O(N)
space comp:- O(h) - recusive stack
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            return 1+max(left, right)
        
        return height(root)
        