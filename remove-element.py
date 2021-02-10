class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = val
        i = 0
        while i < len(nums):
            if ( x == nums[i] ):
                nums.pop(i)
            else:
                i = i + 1
        print (nums)
