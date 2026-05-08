"""
1. standard recurssion, at each node swap the lest and right nodes and call the fun in a loop until it is done for every node
2. return the root node at end of recurrsion
3. if root is none, return none as per testcase

time comp:- O(N)
space comp:- O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left , root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        