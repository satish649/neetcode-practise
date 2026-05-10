"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        node_map = dict()

        def cloneGraphHelper(node):
            if node is None:
                return None

            if node.val in node_map:
                return node_map[node.val]

            clone_node = Node(node.val)
            node_map[node.val] = clone_node

            for neighbor in node.neighbors:
                clone_neighbor = cloneGraphHelper(neighbor)
                clone_node.neighbors.append(clone_neighbor)

            return clone_node
        
        return cloneGraphHelper(node)


        
        
        