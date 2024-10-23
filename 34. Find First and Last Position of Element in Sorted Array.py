class Solution:
    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2

            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid

        return -1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = self.binary_search(nums, target)
        if i ==-1:
            return [-1, -1]
        start = i
        while start > 0 and nums[start - 1] == target:
            start -= 1
        
        end = i
        while end < len(nums) - 1 and nums[end + 1] == target:
            end += 1
        
        return [start, end]
