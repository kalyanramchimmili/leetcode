"""
1. Solved it via both dfs and bfs. we shld return the same graph with new nodes.
2. have a clone fun which clones the val of old node to new node and make a node from it.
3. we cannot link the new node to old node nei, so have a hashmap to store the new node to old node.
4. call the fun recursively to all neighbours until, all nodes are cloned and stored in hashmap, also clone their neightbours to cloned nodes so it forms a graph
5. newNode.neighbors.append(clone(i)), this one by appending the neig of cloned nodes to the clones node and return the first cloned node.

Now using BFS:-
1. use a queue, clone the first node, add the orginal node to queue and store the cloned node against the orignal in a hashmap.
2. if the queue is not empty, by usng left and right pointers, pop the first node, clone its neighbours append the orginals to queue and also hashmap.
3. append the cloned neighbours to the current node i.e first cloned node and continue doing the same for other cloned nodes until queue is empty.

Time comp:- O(N), N being E+v (edges+vertices)
Space comp:- O(V), V being vertices/ all nodes
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
"""