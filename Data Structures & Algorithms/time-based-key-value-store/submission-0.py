class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:

        # print(f"hashmap: {self.hashmap}")
        if key not in self.hashmap:
            return ""

        timestamps = self.hashmap[key]
        (left, right) = (0, len(timestamps) - 1)

        while left <= right:
            mid = (left + right)//2
            print(f"(l, m, r): {left, mid, right} == {timestamps[left], timestamps[mid], timestamps[right]}")
            if timestamps[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        print(f"left: {left}")
        if left == 0:
            return ""

        return timestamps[left - 1][1]
        
