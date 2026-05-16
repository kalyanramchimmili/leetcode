"""

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
# using DFS
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newmap = {}

        if not node:
            return None

        def clone(node):
            if node in newmap:
                return newmap[node]

            newNode = Node(node.val)
            newmap[node] = newNode
            for i in node.neighbors:
                newNode.neighbors.append(clone(i))
            return newNode
        
        return clone(node)
    """

# using BFS
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newmap = {}
        if not node:
            return None
        
        newNode = Node(node.val)
        newmap[node] = newNode
        q = []
        left = 0
        right = 0
        q.append(node)
        right += 1
        while left < right:
            curr_node = q[left]
            left += 1
            for i in curr_node.neighbors:
                if i not in newmap:
                    newNode = Node(i.val)
                    newmap[i] = newNode
                    q.append(i)
                    right += 1

                newmap[curr_node].neighbors.append(newmap[i])

        return newmap[node]