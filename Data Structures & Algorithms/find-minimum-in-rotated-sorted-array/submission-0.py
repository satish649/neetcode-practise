class Solution:
    def findMin(self, nums: List[int]) -> int:

        (left, right) = (0, len(nums) - 1)

        while left <= right:
            mid = (left + right) // 2
            print(f'(l, m, r): {left, mid, right} --> {nums[left], nums[mid], nums[right]}')
            if nums[left] <= nums[right]:
                return nums[left]
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return -1
        