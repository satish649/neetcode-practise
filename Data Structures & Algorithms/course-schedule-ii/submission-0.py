class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for (c, d) in prerequisites:
            graph[d].append(c)
            in_degree[c] += 1
        
        queue = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        ordered_courses = []
        while queue:
            course = queue.popleft()
            ordered_courses.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            
        return ordered_courses if len(ordered_courses) == numCourses else []
        