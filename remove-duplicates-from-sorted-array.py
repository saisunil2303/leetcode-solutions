class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = None
        i = 0
        while i < len(nums):
            if ( x == nums[i] ):
                nums.pop(i)
            else:
                x = nums[i]
                i = i + 1
        print (nums)
