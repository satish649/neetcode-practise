class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        max_heap = []

        for (x,y) in points:
            distance = pow(x, 2) + pow(y, 2)
            heapq.heappush(max_heap, (-distance, (x, y)))
            if (len(max_heap) > k):
                heapq.heappop(max_heap)
        
        ans = []
        for (distance, (x, y)) in max_heap:
            ans.append([x,y])
        
        return ans