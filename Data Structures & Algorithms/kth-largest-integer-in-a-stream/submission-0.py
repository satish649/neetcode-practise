class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.max_elements = k
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if (len(self.min_heap) > self.max_elements):
                heapq.heappop(self.min_heap)
            print(f'heap = {self.min_heap}, length: {len(self.min_heap)}')
        

    def add(self, val: int) -> int:

        heapq.heappush(self.min_heap, val)
        
        if (len(self.min_heap) > self.max_elements):
            heapq.heappop(self.min_heap)
        print(f'heap = {self.min_heap}')
        return self.min_heap[0]
    
        
