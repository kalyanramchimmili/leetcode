"""
1. BFS Problem (Breadth first search). The height of binary tree was DFS.
2. have a res array, level var set at [] and 0 respectively.
3. append a empty [] from level == 1 onwards, to add list within list.
4. append root val if not none, and continue recursively for left and right from the root.
5. Return the ans list.

time comp:- O(N), Each node is visited once.
space comp:- O(N), N:- recursive stack.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        level = 0

        def bfs(root, ans, level):
            if root is None:
                return

            if len(ans) <= level:
                ans.append([])

            ans[level].append(root.val)
            bfs(root.left, ans, level + 1)
            bfs(root.right, ans, level + 1)

        bfs(root, ans, level)
        return ans
