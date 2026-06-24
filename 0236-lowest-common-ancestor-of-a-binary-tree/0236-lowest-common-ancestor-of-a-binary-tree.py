"""
1. dfs, so keep checking until we find the p or q or left node.
2.  if the node is p or q return the node, if not do dfs for that node left and right. for the first ex
        3
       / \
      5   1
     / \
    6   2

for 6 would return 6, then for 2 woulld return 2 the prev dfs would get 6 and 2 for left and right so return root, the right ans here is 5 the lowest common ancestor interms of depth and not value.
3. then dfs(3) would return 5 for left and none for right so return left or right at bottom would return 5 at end of the prog.

time como:- O(N)
space comp:- O(N)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return None
            if root == p or root == q:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            
            if right:
                return right
            else:
                return left
        
        return dfs(root)
        