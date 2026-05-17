class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-weight for weight in stones]
        heapq.heapify(max_heap)

        while max_heap:
            first_stone = -heapq.heappop(max_heap)
            if len(max_heap) == 0:
                return first_stone
            # print(f'len == {len(max_heap)}')
            second_stone = -heapq.heappop(max_heap)

            remaining_weight = first_stone - second_stone
            if remaining_weight > 0:
                heapq.heappush(max_heap, -remaining_weight)
        
        return 0
        