class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for (src, dest) in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        seen = set()
        def dfs(input_node):
            stack = [input_node]
            seen.add(input_node)

            while stack:
                c_node = stack.pop()
                for neighbor in graph[c_node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)

        connected_components = 0
        for i in range(n):
            if i not in seen:
                connected_components += 1
                dfs(i)
        
        return connected_components

        