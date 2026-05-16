"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
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