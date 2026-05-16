class Solution:
    def search(self, nums: List[int], target: int) -> int:

        (left, right) = (0, len(nums)-1)

        def find_rotation_index(nums):
            (left, right) = (0, len(nums)-1)

            while left <= right:

                mid = (left + right)//2

                if nums[left] <= nums[mid] <= nums[right]:
                    return left
                
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid

            return -1

        def binary_search(left, right):

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        
        pivot_index = find_rotation_index(nums)
        found = binary_search(0, pivot_index-1)
        return found if found != -1 else binary_search(pivot_index, len(nums)-1)



        