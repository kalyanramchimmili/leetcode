"""
1. if the root is p or q or root dosent exist return root
2. the returned root is true which mean p and q matched, return the root or parent of it
3. if both didnt match only one did, return the matched node

time comp:- O(N)
space:- O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        if left:
            return left
        
        return right


        