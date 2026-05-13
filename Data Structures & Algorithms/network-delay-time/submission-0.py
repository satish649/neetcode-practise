class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for (u, v, time) in times:
            graph[u].append((v, time))

        # print(f"graph: {graph}")
        
        distances = [math.inf] * (n+1)
        distances[k] = 0

        min_heap = [(0, k)]

        min_time = -1
        while min_heap:
            (curr_distance, node) = heapq.heappop(min_heap)

            if curr_distance > distances[node]:
                continue
            
            for (neighbor, time) in graph[node]:
                new_distance = curr_distance + time
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))
                    if min_time > new_distance:
                        min_time = new_distance
        
        min_time = -math.inf
        for i in range(1, n+1):
            if distances[i] == math.inf:
                return -1
            if distances[i] > min_time:
                min_time = distances[i]
        
        return min_time


        