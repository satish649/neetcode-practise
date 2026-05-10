class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n == 0:
            return True

        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        for (s, d) in edges:
            graph[s].append(d)
            graph[d].append(s)

        queue = deque([0])
        seen = set({0})
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        
        return True if len(seen) == n else False

        
         

        