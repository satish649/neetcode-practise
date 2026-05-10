class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if numCourses == 0:
            return False
        graph = defaultdict(list)
        in_degree_map = defaultdict(int)

        for (src, dest) in prerequisites:
            graph[dest].append(src)
            in_degree_map[src] += 1

        queue = deque()
        for i in range(numCourses):
            if i not in in_degree_map:
                queue.append(i)

        possible_courses = 0
        while queue:
            course = queue.popleft()
            possible_courses += 1
            for neighbour in graph[course]:
                in_degree_map[neighbour] -= 1
                if in_degree_map[neighbour] == 0:
                    queue.append(neighbour)
        
        return True if possible_courses == numCourses else False

        