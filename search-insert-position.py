class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if (target <= nums[i]):
                return i
            elif ( target > nums[i]):
                i = i + 1
        return len(nums)
