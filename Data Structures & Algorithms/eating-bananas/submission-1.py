class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = -math.inf
        for cnt in piles:
            if cnt > right:
                right = cnt
        print(f'right: {right}')
        def calculate_hours_needed(hourly_rate):
            hours_needed = 0
            for cnt in piles:
                hours_needed += math.ceil(cnt/hourly_rate)
            return hours_needed

        while left <= right:
            hourly_rate = (left + right) // 2

            hours_needed = calculate_hours_needed(hourly_rate)
            print(f'(left, right, hourly_rate, hours_needed): {left, right, hourly_rate, hours_needed}')
            
            if hours_needed <= h:
                right = hourly_rate - 1
            else:
                left = hourly_rate + 1

        return left
        