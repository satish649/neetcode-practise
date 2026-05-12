
class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        
    def find(self, node):

        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, nodeX, nodeY):
        rootX = self.find(nodeX)
        rootY = self.find(nodeY)

        if rootX == rootY:
            return False
        
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = self.parent[rootX]
            self.rank[rootX] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        uf = UnionFind(len(edges))

        for (nodeX, nodeY) in edges:
            if uf.union(nodeX, nodeY) == False:
                return [nodeX, nodeY]
        
        return []


